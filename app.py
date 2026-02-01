from flask import Flask, render_template

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


if __name__ == "__main__":
    app.run(debug=True)

