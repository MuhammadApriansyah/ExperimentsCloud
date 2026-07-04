from flask import (
    abort,
    render_template,
    redirect,
    url_for,
    flash,
)

from flask_login import (
    login_required,
    current_user,
)

from app.folders import folders

from app.folders.forms import (
    FolderForm,
    RenameFolderForm,
)

from app.services import FolderService

from app.constants.messages import (
    FLASH_FOLDER_CREATE_SUCCESS,
    FLASH_FOLDER_RENAME_SUCCESS,
    FLASH_FOLDER_DELETE_SUCCESS,
)


@folders.route("/")
@login_required
def index():

    folder_list = FolderService.list_root(
        current_user
    )

    return render_template(
        "folders/index.html",
        folders=folder_list,
    )


@folders.route(
    "/create",
    methods=["GET", "POST"],
)
@login_required
def create():

    form = FolderForm()

    if form.validate_on_submit():

        FolderService.create(
            name=form.name.data,
            owner=current_user,
        )

        flash(
            FLASH_FOLDER_CREATE_SUCCESS,
            "success",
        )

        return redirect(
            url_for("folders.index")
        )

    return render_template(
        "folders/create.html",
        form=form,
    )


@folders.route(
    "/rename/<int:folder_id>",
    methods=["GET", "POST"],
)
@login_required
def rename(folder_id):

    folder = FolderService.get_user_folder(
        folder_id,
        current_user.id,
    )

    if folder is None:
        abort(404)

    form = RenameFolderForm(
        name=folder.name,
    )

    if form.validate_on_submit():

        FolderService.rename(
            folder,
            form.name.data,
        )

        flash(
            FLASH_FOLDER_RENAME_SUCCESS,
            "success",
        )

        return redirect(
            url_for("folders.index")
        )

    return render_template(
        "folders/rename.html",
        form=form,
        folder=folder,
    )


@folders.route(
    "/delete/<int:folder_id>",
    methods=["POST"],
)
@login_required
def delete(folder_id):

    folder = FolderService.get_user_folder(
        folder_id,
        current_user.id,
    )

    if folder is None:
        abort(404)

    FolderService.delete(folder)

    flash(
        FLASH_FOLDER_DELETE_SUCCESS,
        "success",
    )

    return redirect(
        url_for("folders.index")
    )
