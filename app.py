from flask import Flask, app

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

@app.route("/about")
def about():
    return "About Page"

@app.route("/projects")
def projects():
    return "Projects Page"

@app.route("/skills")
def skills():
    return "Skills Page"

@app.route("/contact")
def contact():
    return "Contact Page"

if __name__ == "__main__":
    app.run(debug=True)
