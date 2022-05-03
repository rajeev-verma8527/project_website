from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.secret_key = "key"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact",methods=["GET","POST"])
def contact():
    if request.method == "POST":
        f = request.form
        name = f.get("name")
        email = f.get("email")
        subject = f.get("subject")
        message = f.get("message")
        ## TODO Save data
        flash("Message sent", category="success")
        # return redirect(url_for("index"))
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")
