from flask_wtf import FlaskForm

from wtforms import FileField
from wtforms import StringField
from wtforms import SubmitField

from wtforms.validators import (
    DataRequired,
    Length,
)


class UploadForm(FlaskForm):

    file = FileField(
        "File",
        validators=[
            DataRequired(),
        ],
    )

    submit = SubmitField("Upload")


class RenameFileForm(FlaskForm):

    original_name = StringField(
        "Filename",
        validators=[
            DataRequired(),
            Length(min=1, max=255),
        ],
    )

    submit = SubmitField("Rename")
