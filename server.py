from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import logging
import time

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# GraphQL API endpoint
GRAPHQL_URL = "http://coreexplorer.org/api/graphql"

# Function to execute GraphQL query with retry logic
def execute_graphql_query(query, retries=3, backoff_factor=2):
    for attempt in range(retries):
        try:
            logger.debug(f"Attempt {attempt + 1}: Sending GraphQL query to {GRAPHQL_URL}: {query}")
            response = requests.post(GRAPHQL_URL, json={"query": query}, timeout=None)
            logger.debug(f"Response status: {response.status_code}, content: {response.text}")
            if response.status_code == 200:
                return response.json()
            else:
                logger.error(f"HTTP error: {response.status_code}, response: {response.text}")
                if response.status_code == 504:
                    logger.warning("Gateway timeout detected, retrying...")
                    time.sleep(backoff_factor ** attempt)
                    continue
                return {"errors": f"HTTP error: {response.status_code}"}
        except requests.exceptions.RequestException as e:
            logger.error(f"Request exception: {str(e)}")
            if "timeout" in str(e).lower() or "gateway" in str(e).lower():
                logger.warning(f"Timeout or gateway error, retrying after {backoff_factor ** attempt} seconds...")
                time.sleep(backoff_factor ** attempt)
                continue
            return {"errors": str(e)}
    logger.error("Max retries reached, failing...")
    return {"errors": "Failed after max retries due to timeout or gateway error"}

# Route to serve the test.html page
@app.route('/')
def serve_test():
    return render_template('test.html')

# Generic endpoint to pass through GraphQL queries
@app.route('/api/query', methods=['POST'])
def handle_query():
    try:
        data = request.get_json()
        if not data or 'query' not in data:
            logger.error("Invalid request: No query provided in request body")
            return jsonify({"error": "Query is required"}), 400

        query = data['query']
        logger.debug(f"Received query from client: {query}")

        result = execute_graphql_query(query)
        logger.debug(f"API response: {result}")

        return jsonify(result)
    except Exception as e:
        logger.error(f"Error in handle_query: {str(e)}", exc_info=True)
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)