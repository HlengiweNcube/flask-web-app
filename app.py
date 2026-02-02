from flask import Flask, render_template, request

app = Flask(__name__)

projects = [
    {
        "title": "Afrovibes – Southern African Music Showcase",
        "description": (
            "An HTML-based website created to showcase Southern African music and culture. "
            "The project highlights iconic artists such as Miriam Makeba, groups like Ladysmith Black Mambazo "
            "and Asungura Boys, and traditional instruments including the mbira and African drums. "
            "The site focuses on structure, content presentation, and cultural storytelling using HTML."
        ),
        "image": "ladysmith.jpg"
    },
    {
        "title": "Tour Zimbabwe – Interactive Travel Website",
        "description": (
            "A web project built using HTML and JavaScript to promote tourism in Zimbabwe. "
            "The website features popular destinations such as Victoria Falls, the Zambezi Valley, "
            "Matobo Hills, and other attractions. JavaScript was used to add interactivity and enhance "
            "the user experience."
        ),
        "image": "lion.jpg"
    }
]

skills = [
    "Python",
    "Flask",
    "HTML",
    "CSS",
    "JavaScript"
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

@app.route("/skills")
def skills_page():
    return render_template("skills.html", skills=skills)

@app.route("/about")
def about_page():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)

