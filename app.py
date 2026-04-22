from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "secret123"  # REQUIRED for flash messages

projects = [
    {
        "id": 0,
        "title": "Afrovibes – Southern African Music Showcase",
        "description": "Music and culture showcase project.",
        "image": "ladysmith.jpg",
        "live_url": "https://hlengiwencube.github.io/afrovibes/"
    },
    {
        "id": 1,
        "title": "Tour Zimbabwe – Interactive Travel Website",
        "description": "Tourism web app with JavaScript interactivity.",
        "image": "lion.jpg",
        "live_url": "https://hlengiwencube.github.io/tour_zimbabwe/"
    }
]

skills = ["Python", "Flask", "HTML", "CSS", "JavaScript"]

# HOME
@app.route("/")
def home():
    return render_template("home.html", projects=projects, skills=skills)

# PROJECTS
@app.route("/projects")
def projects_page():
    return render_template("projects.html", projects=projects)

# SKILLS
@app.route("/skills")
def skills_page():
    return render_template("skills.html", skills=skills)

# ABOUT
@app.route("/about")
def about_page():
    return render_template("about.html")

# CONTACT
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not phone or not message:
            flash("All fields are required.")
            return redirect(url_for("contact"))

        if not phone.isdigit():
            flash("Phone must contain digits only.")
            return redirect(url_for("contact"))

        flash("Thank you! Your message has been sent.")
        return redirect(url_for("contact"))

    return render_template("contact.html")

# GET PROJECT 
def get_project(project_id):
    return next((p for p in projects if p["id"] == project_id), None)

# EDIT PROJECT (UPDATE)
@app.route("/edit_project/<int:project_id>", methods=["GET", "POST"])
def edit_project(project_id):
    project = get_project(project_id)

    if project is None:
        flash("Project not found.")
        return redirect(url_for("projects_page"))

    if request.method == "POST":
        project["title"] = request.form.get("title")
        project["description"] = request.form.get("description")
        flash("Project updated!")
        return redirect(url_for("projects_page"))

    return render_template("edit_project.html", project=project)

# DELETE PROJECT
@app.route("/delete_project/<int:project_id>")
def delete_project(project_id):
    global projects
    projects = [p for p in projects if p["id"] != project_id]

    flash("Project deleted!")
    return redirect(url_for("projects_page"))

@app.route("/add_project", methods=["GET", "POST"])
def add_project():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        image = request.form.get("image")
        live_url = request.form.get("live_url")

        if not title or not description:
            flash("Title and description are required.")
            return redirect(url_for("add_project"))

        new_project = {
            "id": len(projects),
            "title": title,
            "description": description,
            "image": image if image else "default.jpg",
            "live_url": live_url if live_url else "#"
        }

        projects.append(new_project)

        flash("Project added successfully!")
        return redirect(url_for("projects_page"))

    return render_template("add_project.html")

skills = [
    {"name": "HTML", "desc": "Semantic structure and layout"},
    {"name": "JavaScript", "desc": "DOM manipulation and events"},
    {"name": "Flask", "desc": "Routing and backend logic"}
]

if __name__ == "__main__":
    app.run(debug=True)