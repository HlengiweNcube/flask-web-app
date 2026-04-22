from flask import Flask, render_template, request, flash, redirect, url_for
import re
from data import projects, skills

app = Flask(__name__)
app.secret_key = "secret123"


def get_project(project_id: int):
    return next((p for p in projects if p["id"] == project_id), None)


def validate_contact(name, email, phone, message):
    if not name or not email or not phone or not message:
        return "All fields are required."
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
        return "Please enter a valid email."
    if not re.match(r"^\d{7,15}$", phone):
        return "Phone must be 7-15 digits."
    if len(message) < 10:
        return "Message must be at least 10 characters."
    return None


@app.route("/")
def home():
    return render_template("home.html", projects=projects, skills=skills)


@app.route("/projects")
def projects_page():
    return render_template("projects.html", projects=projects)


@app.route("/project/<int:project_id>")
def project_detail(project_id):
    project = get_project(project_id)
    if project is None:
        flash("Project not found.")
        return redirect(url_for("projects_page"))
    return render_template("project_detail.html", project=project)


@app.route("/skills")
def skills_page():
    return render_template("skills.html", skills=skills)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        message = request.form.get("message", "").strip()

        error = validate_contact(name, email, phone, message)
        if error:
            flash(error)
            return redirect(url_for("contact"))

        flash("Thank you! Your message has been sent.")
        return redirect(url_for("home"))

    return render_template("contact.html")


@app.route("/edit_project/<int:project_id>", methods=["GET", "POST"])
def edit_project(project_id):
    project = get_project(project_id)
    if project is None:
        flash("Project not found.")
        return redirect(url_for("projects_page"))

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()

        if not title or not description:
            flash("Title and description are required.")
            return redirect(url_for("edit_project", project_id=project_id))

        project["title"] = title
        project["description"] = description
        flash("Project updated!")
        return redirect(url_for("projects_page"))

    return render_template("edit_project.html", project=project)


@app.route("/delete_project/<int:project_id>")
def delete_project(project_id):
    project = get_project(project_id)
    if project is None:
        flash("Project not found.")
        return redirect(url_for("projects_page"))

    projects.remove(project)
    flash("Project deleted!")
    return redirect(url_for("projects_page"))


@app.route("/add_project", methods=["GET", "POST"])
def add_project():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        image = request.form.get("image", "").strip() or "default.jpg"
        live_url = request.form.get("live_url", "").strip() or "#"

        if not title or not description:
            flash("Title and description are required.")
            return redirect(url_for("add_project"))

        new_id = max((p["id"] for p in projects), default=-1) + 1
        projects.append(
            {
                "id": new_id,
                "title": title,
                "description": description,
                "image": image,
                "live_url": live_url,
            }
        )

        flash("Project added successfully!")
        return redirect(url_for("projects_page"))

    return render_template("add_project.html")


if __name__ == "__main__":
    app.run(debug=True)