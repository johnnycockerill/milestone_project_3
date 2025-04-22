from flask import render_template
from schedule_manager import app, db  # noqa
from schedule_manager.models import Service, Vehicle  # noqa


@app.route("/")
def home():
    return render_template("vehicles.html")
