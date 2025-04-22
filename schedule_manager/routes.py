from flask import render_template
from schedule_manager import app, db  # noqa


@app.route("/")
def home():
    return render_template("base.html")