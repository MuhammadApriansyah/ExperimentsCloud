from flask import Blueprint

folders = Blueprint(
    "folders",
    __name__,
    url_prefix="/folders",
)
