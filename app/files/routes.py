from flask import render_template

from pathlib import Path

from flask import (
    abort,
    send_file,
    redirect,
    render_template,
    send_file,
    url_for,
    flash,
)
from flask_login import (
    current_user,
    login_required,
)
from app.files.forms import UploadForm

from app.constants.messages import (
    FLASH_UPLOAD_SUCCESS,
    FLASH_DELETE_SUCCESS,
)

from app.files import files
from app.files.services import FileService
from app.services.storage_service import StorageService
from app.services.logging_service import logger

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

@files.route("/download/<int:file_id>")
@login_required
def download(file_id):

    file = FileService.get_user_file(
        file_id,
        current_user.id
    )

    if file is None:
        abort(404)

    path = StorageService.file_path(
        current_user.id,
        file.stored_name,
    )

    if not StorageService.exists(path):
        abort(404)

    logger.info(
        "DOWNLOAD | user=%s | file=%s",
        current_user.id,
        file.original_name,
    )

    return send_file(
        path,
        as_attachment=True,
        download_name=file.original_name,
    )

@files.route("/delete/<int:file_id>", methods=["POST"])
@login_required
def delete(file_id):

    file = FileService.get_user_file(
        file_id,
        current_user.id,
    )

    if file is None:
        abort(404)

    FileService.delete(file)

    logger.info(
        "DELETE | user=%s | file=%s",
         current_user.id,
         file.original_name,
    )

    flash(
        FLASH_DELETE_SUCCESS,
        "success",
    )

    return redirect(
        url_for("files.index")
    )
