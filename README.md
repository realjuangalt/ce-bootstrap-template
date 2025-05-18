# Core Explorer Bootstrap Template

## Overview
The `general_template.html` serves as a reusable bootstrap template for the Core Explorer website, a data science interface for analyzing software projects, starting with the Bitcoin Core repository. This template provides a responsive, visually consistent layout with a header, main content area, and footer, designed to be extensible for other pages. It uses Bootstrap 4.3.1, Font Awesome 5.15.4, and custom CSS/JavaScript to deliver a modern, theme-switchable interface (dark mode with orange glow, light mode with black glow/thicker borders).

## Features
- **Responsive Header**:
  - **Wide Screen (≥992px)**: Navbar brand (logo, "Core Explorer") left; navigation icons (GitHub, mail, theme toggle), search bar, and search button right.
  - **Mobile (<992px)**: Two rows:
    - Top: Navbar brand left, navigation icons (GitHub, mail, theme toggle) right.
    - Bottom: Search bar (expands to search button) left, search button right.
- **Main Content**:
  - Centered project title ("Welcome to Core Explorer") and description ("A data science visualizer for the Bitcoin Core repository").
  - Stats display:
    - Mobile: Table format (Lines of Code: 3,214, Files: 4,321, Commits: 44,727), full-width, right-aligned, `.box` styling.
    - Wide screen: Row format ("Lines of Code 3,214 | Files 4,321 | Commits 44,727"), centered below description, `.box` styling.
  - Two placeholders (Neo4j graph, heat map), 300px height, `.box` styling, 15px vertical padding between them.
- **Footer**:
  - Centered navigation icons (GitHub, mail, theme toggle), no border/shadow/background, floating on page background.
- **Theme Switching**:
  - Dark mode: Orange text/borders (`#f7931a`), glow (`box-shadow: 0 0 8px rgba(247, 147, 26, 0.3)`), dark backgrounds (`#1a1a1a`, `#2d2d2d`, `#1f1f1f`).
  - Light mode: Blue text/borders (`#007bff`), black glow/thicker borders, light backgrounds (`#ffffff`, `#f8f9fa`, `#e9ecef`).
  - Theme toggle buttons in header and footer, synchronized.
- **Responsive Design**:
  - Breakpoints: <576px (small mobile), <992px (mobile), ≥600px (larger elements), ≥992px (wide screen).
  - Flexbox layout for consistent positioning and centering.

## Dependencies
- **Bootstrap 4.3.1**:
  - CSS: `https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css`
  - JS: `https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js`
  - Requires: jQuery 3.3.1 slim (`https://code.jquery.com/jquery-3.3.1.slim.min.js`), Popper.js 1.14.7 (`https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js`)
- **Font Awesome 5.15.4**:
  - CSS: `https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css`
  - Icons: GitHub (`fab fa-github`), mail (`fas fa-envelope`), theme toggle (`fas fa-moon`/`fas fa-sun`), search (`fas fa-search`).
- **External Assets**:
  - Core Explorer logo: `https://i.imgur.com/0cx91au.png`

## File Structure
```
core-explorer/
└── general_template.html  # Main template file (HTML, inline CSS, JavaScript)
```

## Technical Details
### HTML Structure
- **Body**:
  - Flexbox column layout (`display: flex; flex-direction: column; min-height: 100vh`) to ensure footer stays at bottom.
  - Contains: `<nav>`, `<div class="content-container">`, `<footer>`.
- **Navbar**:
  - `<nav class="navbar navbar-expand-lg navbar-dark box">` with `.navbar-top` (brand left, `.navbar-nav` right) and `.search-container` (search bar, button).
  - Mobile: `.navbar-top` for top row, `.search-container` for bottom row.
  - Wide: `.search-container` includes `.navbar-nav`, search bar, button, right-aligned.
- **Content Container**:
  - `<div class="container-fluid content-container box">` with flex: 1 to fill space.
  - Contains `<main>` with:
    - `.project-section`: Centered `.project-details` (title, description), stats (`.stat-table` mobile, `.stat-row` wide).
    - Two `.graphic-placeholder` divs (Neo4j, heat map).
- **Footer**:
  - `<footer>` with centered `.navbar-nav`.

### CSS
- **Theme Variables**:
  - Defined in `:root` and `body.light-mode`:
    - `--bs-body-bg`, `--bs-body-color`, `--bs-primary`, `--bs-secondary`, `--bs-tertiary-bg`, `--bs-link-hover-color`, `--bs-border-color`, `--bs-border-radius`, `--bs-border-radius-sm`, `--bs-button-border-radius`, `--bs-focus-ring-color`.
  - Example: Dark mode `--bs-body-bg: #1a1a1a`, light mode `--bs-body-bg: #ffffff`.
- **Box Styling**:
  - `.box`: `background-color: var(--bs-secondary)`, `border: 1px solid var(--bs-border-color)` (2px light mode), `border-radius: var(--bs-border-radius)`, `padding: 10px`, `box-shadow: 0 0 8px rgba(var(--bs-primary-rgb), 0.3)` (black light mode).
  - Applied to: `.navbar`, `.content-container`, `.stat-table`, `.stat-row`, `.graphic-placeholder`.
- **Navbar Buttons**:
  - `.nav-link`, `.theme-toggle-btn`: `font-size: 1em`, `padding: 6px 8px`, `line-height: 1.5`, `width: 32px`, `height: 32px`, `display: inline-flex`, `align-items: center`, `justify-content: center`, `text-align: center`, no borders/glow, hover (`background-color: #555` dark, `#bbb` light).
- **Search Bar/Button**:
  - `.search-bar`: `background-color: var(--bs-tertiary-bg)`, `border: 1px solid var(--bs-border-color)`, `width: 200px` (wide: `250px`, mobile: `calc(100% - 36px)`), `font-size: 1em` (mobile: `0.9em`).
  - `.search-btn`: Matches `.nav-link` styling, `width: 32px`, `height: 32px`.
- **Stats**:
  - Mobile: `.stat-table.box` with table (three rows, names left, numbers right), full-width, right-aligned.
  - Wide: `.stat-row.box` with flex row ("Lines of Code 3,214 | Files 4,321 | Commits 44,727"), centered, `padding: 10px`.
- **Placeholders**:
  - `.graphic-placeholder`: `height: 300px`, `background-color: var(--bs-tertiary-bg)`, `border: 1px solid var(--bs-border-color)`, `margin-bottom: 15px`, centered text.
- **Responsive Breakpoints**:
  - `<576px`: Smaller fonts (`h3: 1.2em`, `p: 0.8em`), search bar `font-size: 0.9em`.
  - `<992px`: Mobile layout (header two rows, stats table).
  - `≥600px`: Larger logo (`48px`), title (`1.2em`), search bar (`250px`).
  - `≥992px`: Wide layout (header single row, stats row).

### JavaScript
- **Theme Toggle**:
  - `toggleTheme()`: Toggles `light-mode` class on `body`, switches `.navbar` between `navbar-dark` and `navbar-light`, updates header/footer theme toggle icons (moon/sun).
  - Event listeners on `theme-toggle-header` and `theme-toggle-footer`.
- **Dependencies**: jQuery slim for Bootstrap, no additional logic required.

## Usage Instructions
1. **Setup**:
   - Copy `general_template.html` to your project directory.
   - Ensure internet access for CDN dependencies (Bootstrap, Font Awesome, jQuery, Popper.js).
   - Alternatively, download dependencies and host locally, updating `<link>` and `<script>` sources.

2. **Customization**:
   - **Header**:
     - Modify logo in `.navbar-brand` (`<img src="...">`).
     - Update `.navbar-nav` links/icons (e.g., change GitHub/mail URLs).
     - Adjust search bar placeholder or add functionality in `.search-bar`.
   - **Main Content**:
     - Update `.project-details` title (`<h3>`) and description (`<p>`).
     - Modify stats in `.stat-table` (mobile) and `.stat-row` (wide screen) with new data.
     - Replace `.graphic-placeholder` content with actual visualizations (e.g., Neo4j graphs, heat maps).
   - **Footer**:
     - Customize `.navbar-nav` links/icons to match header or add new ones.
   - **Theme**:
     - Adjust theme variables in `:root` and `body.light-mode` (e.g., colors, borders).
     - Extend `toggleTheme()` for additional theme-dependent elements.
   - **Styling**:
     - Update `.box` for different borders/shadows.
     - Modify `.graphic-placeholder` dimensions (`height: 300px`) or styling.
     - Adjust responsive breakpoints in media queries.

3. **Extending for New Pages**:
   - Create a new HTML file based on `general_template.html`.
   - Replace `.content-container` content with page-specific elements, reusing `.box`, `.navbar-nav`, and other classes for consistency.
   - Maintain flexbox layout (`body { display: flex; flex-direction: column; min-height: 100vh }`) for footer positioning.
   - Example: Add new sections with `.box` styling, use `.navbar-nav` for navigation, or extend `.graphic-placeholder` for visualizations.

4. **Testing**:
   - Test responsiveness across devices (mobile: <576px, <992px; wide: ≥992px).
   - Verify theme switching (dark/light) in different lighting conditions.
   - Check icon alignment (`32px x 32px`) and hover effects.
   - Ensure placeholders and stats render correctly in both modes.

## Customization Examples
- **Change Logo**:
  ```html
  <a class="navbar-brand" href="#">
    <img src="new-logo.png" alt="New Logo" class="cek-logo">
    <span class="navbar-brand-text">
      <span>New</span>
      <span>Title</span>
    </span>
  </a>
  ```
- **Update Stats**:
  ```html
  <div class="stat-row box">
    <div class="stat-item">
      <span class="stat-label">New Metric</span>
      <span class="stat-value">1,000</span>
    </div>
    <span class="stat-divider">|</span>
    <div class="stat-item">
      <span class="stat-label">Another</span>
      <span class="stat-value">2,000</span>
    </div>
  </div>
  ```
- **Add New Placeholder**:
  ```html
  <div class="graphic-placeholder">
    [Placeholder for new visualization]
  </div>
  ```
- **Modify Theme Colors**:
  ```css
  :root {
    --bs-primary: #ff0000; /* Red glow */
    --bs-body-color: #ff0000;
    --bs-primary-rgb: 255, 0, 0;
  }
  ```

## Known Limitations
- **Search Functionality**: `.search-bar` and `.search-btn` are placeholders (no event listeners or backend).
- **Static Data**: Stats (3,214, 4,321, 44,727) are mock data; requires API integration for dynamic data.
- **Placeholders**: Neo4j and heat map placeholders are static; need visualization libraries (e.g., vis.js, D3.js) for implementation.
- **Accessibility**: Lacks ARIA attributes and keyboard navigation; add for production use.

## Future Enhancements
- Implement search functionality with GitHub API integration.
- Replace placeholders with dynamic visualizations (Neo4j graphs, heat maps).
- Add accessibility features (ARIA labels, keyboard support).
- Split CSS/JavaScript into separate files for larger projects.
- Integrate dynamic stats via GitHub API.
- Test across additional browsers/devices (e.g., Safari, Edge, iOS/Android).

## Contributing
- Fork the repository and modify `general_template.html`.
- Submit pull requests with clear descriptions of changes.
- Ensure responsiveness, theme consistency, and no dependency conflicts.
- Test changes in both dark and light modes.

## License
This template is provided under the MIT License. See `LICENSE` for details (if applicable).