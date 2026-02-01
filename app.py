from flask import Flask, render_template, request

app = Flask(__name__)

projects = [
    {
        "title": "Flask Web App",
        "description": "A simple web application built using Flask."
    },
    {
        "title": "Portfolio Website",
        "description": "A personal portfolio showcasing projects and skills."
    }
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/projects")
def projects_page():
    return render_template("projects.html", projects=projects)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        return f"Thank you {name}, your message has been received!"

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

