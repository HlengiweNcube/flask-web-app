from flask import Flask, render_template, request,flash

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
        "image": "ladysmith.jpg",
        "live_url": "https://hlengiwencube.github.io/afrovibes/"
        
    },    {
        "title": "Tour Zimbabwe – Interactive Travel Website",
        "description": (
            "A web project built using HTML and JavaScript to promote tourism in Zimbabwe. "
            "The website features popular destinations such as Victoria Falls, the Zambezi Valley, "
            "Matobo Hills,Bulawayo City Hall, the vibrant capital city Harare and other attractions. JavaScript was used to add interactivity and enhance "
            "the user experience."
        ),
        "image": "lion.jpg",
        "live_url": "https://hlengiwencube.github.io/tour_zimbabwe/"
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
def contact_page():
    
    return render_template("contact.html")

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

        if not name or not email or not phone or not message:
            flash("All fields are required.")
            return render_template("contact.html")

        if not phone.isdigit():
            flash("Phone number must contain digits only.")
            return render_template("contact.html")

        # If everything is valid
        flash("Thank you! Your message has been sent.")
        return render_template("contact.html")

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

