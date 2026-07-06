from flask import Flask, render_template

from app.config import get_config

from app.extensions import db
from app.extensions import migrate
from app.extensions import login_manager

from app.auth.routes import auth
from app.files import files

from app.utils.file_utils import human_size
from app.utils.date_utils import human_datetime

from app.errors import errors

from app.folders.routes import folders

from app.helpers import (
    format_file_size,
    get_file_icon,
    get_file_type,
)

def create_app(config_object=None):

    app = Flask(__name__)

    if config_object is None:
        app.config.from_object(get_config())
    else:
        app.config.from_object(config_object)

    app.jinja_env.globals.update(
        format_file_size=format_file_size,
        get_file_icon=get_file_icon,
        get_file_type=get_file_type,
    )

    db.init_app(app)

    login_manager.init_app(app)

    migrate.init_app(app, db)

    @app.route("/")
    def home():
        return render_template("home.html")

    app.register_blueprint(auth)
    app.register_blueprint(files)
    app.register_blueprint(folders)
    app.register_blueprint(errors)

    app.jinja_env.filters["human_size"] = human_size

    app.jinja_env.filters["human_datetime"] = human_datetime

    return app
