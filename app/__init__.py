from flask import Flask, render_template

from app.config import Config
from app.extensions import db
from app.extensions import migrate
from app.extensions import login_manager

from app.auth import auth

from app.auth.routes import auth
from app.files import files

from app.utils.file_utils import human_size
from app.utils.date_utils import human_datetime

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    login_manager.init_app(app)

    migrate.init_app(app, db)

    @app.route("/")
    def home():
        return render_template("home.html")

    app.register_blueprint(auth)
    app.register_blueprint(files)

    app.jinja_env.filters["human_size"] = human_size

    app.jinja_env.filters["human_datetime"] = human_datetime

    return app
