# Flask Portfolio Web Application

## 📌 Project Overview
This project is a web application built using **Python and Flask** as part of a course assignment.  
The purpose of the application is to demonstrate the use of Flask for backend development while integrating **HTML, CSS, and JavaScript** to create a modern, interactive, and visually appealing website.

The web application functions as a **personal portfolio website** that showcases projects, skills, background information, and includes a contact form. The application is deployed online using **Render.com**.

---

## 🎯 Project Objectives
- Build a dynamic web application using Flask
- Implement multiple routes and HTML templates
- Apply modern CSS styling for a professional appearance
- Add JavaScript functionality for interactivity
- Handle HTTP methods (GET and POST)
- Deploy a Flask application using Render.com

---


## 🧭 Development Approach

Rather than producing a separate planning document,  
**design decisions and iterations were documented continuously**
and are recorded below.

This reflects a realistic development workflow where planning,
testing, and refinement occur alongside implementation.

---

## Application Features

### Core Pages

| Page     | Description |
|----------|-------------|
| Home     | Introduction and navigation hub |
| Projects | Displays a list of projects using Flask data structures |
| Skills   | Shows technical skills dynamically |
| About    | Background and personal information |
| Contact  | Contact form using POST request |

## Interactive Features
- Navigation menu across all pages
- Smooth scrolling via JavaScript
- Form submission handling on the Contact page
- Responsive and modern layout using CSS

## Technologies Used

### Backend
- Python  
- Flask  

### Frontend
- HTML5  
- CSS3  
- JavaScript  

### Deployment
- GitHub  
- Render.com  

---

## 🧩 Site Structure & Navigation

The website consists of the following pages:

- Home
- About
- Skills
- Projects
- Contact

### Navigation Design
- **Tried:** fixed and repositioned navigation
- **Issue:** jumpy experience when scrolling
- **Selected:** consistent static navigation across all pages
- **Reason:** improves usability and orientation

Active navigation links are highlighted to show the current page.

---

## 🖼️ Layout & Visual Design

### Layout Choice
- **Tried:** Flexbox-only layouts
- **Issue:** limited control for card-based layouts
- **Selected:** CSS Grid for cards and sections
- **Reason:** Grid provides better responsiveness and alignment

### Page Structure
- Hero sections used to visually indicate the start of pages
- Cards used to group related content
- Containers used to control content width on large screens

---

## 🎨 CSS Design Decisions

- Reusable classes were created to reduce duplication
- Gradients were used for hero sections and navigation for visual consistency
- Hover and focus states were added for interactive element
## Project Structure

flask_web_app/
│
├── app.py
├── README.md
│
├── templates/
│ └── home.html
│
├── static/
│ ├── css/
│ │ └── style.css
│ └── js/
│ └── script.js
│
├── venv/


## How to Run the Project Locally

1. Clone the repository:
    git clone <repository-url>
 
2. Navigate into the project folder:
   cd flask_web_app

3. Create and activate a virtual environment:
   python -m venv venv
   source venv/Scripts/activate

4. Install the required dependencies:
   pip install flask

5. Run the Flask application:
  python app.py

6. Open a web browser and go to:
 http://127.0.0.1:5000/

## Application Features

### Core Pages

| Page     | Description |
|----------|-------------|
| Home     | Introduction and navigation hub |
| Projects | Displays a list of projects using Flask data structures |
| Skills   | Shows technical skills dynamically |
| About    | Background and personal information |
| Contact  | Contact form using POST request |

---

## ♿ Accessibility Considerations

Accessibility was considered throughout the development of this project:

- Semantic HTML elements were used (`header`, `nav`, `main`, `section`)
- A skip-to-content link was implemented for keyboard users
- Visible focus styles were added for links, buttons, and form fields
- Form inputs use appropriate input types and labels
- Images include descriptive alt text

These decisions were made to improve usability for keyboard and screen reader users.

---

## ✅ Validation

The project was checked for standards compliance:

- HTML validated using the W3C HTML Validator
- CSS validated using the W3C CSS Validator

Any warnings or errors encountered were reviewed and resolved where possible to ensure clean, standards-compliant code.

## References & Credits

Learning resources used during development include:

- Flask official documentation
- MDN Web Docs (HTML, CSS, JavaScript)
- W3Schools (syntax reference)

Images used in the project were sourced from free-to-use platforms:

- Unsplash
- Pexels

## 🔗 External Project Links

Some projects showcased in this portfolio were created earlier in the course
using standalone HTML and JavaScript, before Flask was introduced.

These projects are linked as **external live sites** and open in a new browser tab.
This design choice ensures that users do not lose their place within the Flask
portfolio application while viewing earlier work.

Due to the static nature of these earlier projects, there is no automatic
navigation back to the Flask application unless a manual link is added.
This limitation is acknowledged and was intentionally accepted to avoid
modifying completed coursework retrospectively.

