from flask import Flask, render_template, request, redirect, url_for, flash
from database import save_info

app = Flask(__name__)

app.secret_key = "key"

city_templates = {
    "agra": ["taj",],
    "lucknow": ["imambara",],
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        f = request.form
        name = f.get("name")
        email = f.get("email")
        subject = f.get("subject")
        message = f.get("message")
        save_info(name, email, subject, message)
        flash("Message sent", category="success")

    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/cities/<city>")
def cities(city):
    return render_template("album_layout.html", locations=["cities/agra/taj.html"])


# @app.route("/locations/<location>")
# def locations(location):
#     pass
