from flask import render_template

from flask_login import login_required

from app.files import files

from flask import (
    flash,
    redirect,
    url_for,
)

from app.files.forms import UploadForm

from app.files.services import FileService

from app.constants.messages import (
    FLASH_UPLOAD_SUCCESS,
)

from flask_login import current_user

from app.files.services import FileService


@files.route("/")
@login_required
def index():

    files = FileService.list_files(
        current_user
    )

    return render_template(
        "files/index.html",
        files=files,
    )


@files.route("/upload", methods=["GET", "POST"])
@login_required
def upload():

    form = UploadForm()

    if form.validate_on_submit():

        FileService.upload(
            form.file.data
        )

        flash(
            FLASH_UPLOAD_SUCCESS,
            "success",
        )

        return redirect(
            url_for("files.index")
        )

    return render_template(
        "files/upload.html",
        form=form,
    )
