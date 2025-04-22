from flask import render_template
from schedulemanager import app, db  # noqa
from schedulemanager.models import Service, Vehicle  # noqa


@app.route("/")
def home():
    return render_template("vehicles.html")
