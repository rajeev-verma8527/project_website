from flask import Flask, render_template, request, redirect, url_for, flash
from database import save_info
from aggregate_templates import get_tree
import os
import random


app = Flask(__name__)

app.secret_key = "this_is_a_totally_random_key_that_is_definitely_safe_and_secure"

city_templates = get_tree(os.getcwd())
all_locations = []
for city in city_templates:
    for loc in city_templates[city]:
        all_locations.append(f"cities/{city}/{loc}")

@app.route("/")
def index():
    if request.args.get("all"):
        return render_template("index.html",locations=all_locations)
    else:
        return render_template("index.html",locations=random.sample(all_locations,12))

@app.route("/cities/<city>")
def cities(city):
    if city in city_templates:
        locations = [f"cities/{city}/{i}" for i in city_templates[city]]
        return render_template(f"cities/{city}/main.html", locations=locations, title=city.title())
    return render_template("error.html"), 404

@app.route("/locations/<location>")
def locations(location):
    for city,locations in city_templates.items():
        if (location + ".html") in locations:
            return render_template(f"cities/{city}/{location}.html")
    return render_template("error.html"), 404 






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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404