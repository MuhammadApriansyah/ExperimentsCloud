from flask import render_template

from flask_login import login_required

from app.files import files


@files.route("/")
@login_required
def index():
    return render_template("files/index.html")
