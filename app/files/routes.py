from pathlib import Path

from flask import (
    abort,
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

from app.files.forms import (
    UploadForm,
    RenameFileForm,
)

from app.constants.messages import (
    FLASH_UPLOAD_SUCCESS,
    FLASH_DELETE_SUCCESS,
    FLASH_RENAME_SUCCESS,
)

from app.files import files
from app.files.services import FileService
from app.services.logging_service import logger
from app.storage.manager import get_storage

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
            form.file.data,
            current_user,
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
        current_user.id,
    )

    if file is None:
        abort(404)

    storage = get_storage()

    path = storage.file_path(
        current_user.id,
        file.stored_name,
    )

    print(path)
    print(storage.exists(path))

    if not storage.exists(path):
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

@files.route(
    "/rename/<int:file_id>",
    methods=["GET", "POST"],
)
@login_required
def rename(file_id):

    file = FileService.get_user_file(
        file_id,
        current_user.id,
    )

    if file is None:
        abort(404)

    form = RenameFileForm(
        original_name=Path(file.original_name).stem,
    )

    if form.validate_on_submit():

        FileService.rename(
            file,
            form.original_name.data,
        )

        flash(
            FLASH_RENAME_SUCCESS,
            "success",
        )

        return redirect(
            url_for("files.index")
        )

    return render_template(
        "files/rename.html",
        form=form,
        file=file,
    )

