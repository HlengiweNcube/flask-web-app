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

## 📂 Project Structure

flask_portfolio/
│
├── app.py
├── requirements.txt
│
├── templates/
│   ├── home.html
│   ├── projects.html
│   ├── skills.html
│   ├── about.html
│   └── contact.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js


## Flask Routes Plan

| Route       | HTTP Method | Purpose                        |
| ----------- | ----------- | ------------------------------ |
| `/`         | GET         | Load home page                 |
| `/projects` | GET         | Display project list           |
| `/skills`   | GET         | Display skills                 |
| `/about`    | GET         | Show about page                |
| `/contact`  | GET, POST   | Handle contact form submission |

