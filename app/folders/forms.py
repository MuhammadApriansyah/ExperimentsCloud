from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    SubmitField,
)

from wtforms.validators import (
    DataRequired,
    Length,
)


class FolderForm(FlaskForm):

    name = StringField(
        "Folder Name",
        validators=[
            DataRequired(),
            Length(
                min=1,
                max=255,
            ),
        ],
    )

    submit = SubmitField(
        "Create Folder"
    )


class RenameFolderForm(FlaskForm):

    name = StringField(
        "Folder Name",
        validators=[
            DataRequired(),
            Length(
                min=1,
                max=255,
            ),
        ],
    )

    submit = SubmitField(
        "Rename Folder"
    )
