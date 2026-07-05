from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    request
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


from app.helpers import (
    get_owned_folder_or_404,
)

from app.files.services import FileService


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
    "/<int:folder_id>",
)
@login_required
def open(folder_id):

    folder = get_owned_folder_or_404(
        folder_id,
        current_user.id,
    )

    children = FolderService.list_children(
        folder,
    )

    files = FileService.list_files(
        current_user,
        folder,
    )

    return render_template(
        "folders/index.html",
        folders=children,
        files=files,
        current_folder=folder,
        path=FolderService.build_path(folder),
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

    folder = get_owned_folder_or_404(
        folder_id,
        current_user.id,
    )

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

    folder = get_owned_folder_or_404(
        folder_id,
        current_user.id,
    )

    FolderService.delete(folder)

    flash(
        FLASH_FOLDER_DELETE_SUCCESS,
        "success",
    )

    return redirect(
        url_for("folders.index")
    )


@folders.route(
    "/<int:folder_id>/upload",
    methods=["POST"],
)
@login_required
def upload(folder_id):

    folder = get_owned_folder_or_404(
        folder_id,
        current_user.id,
    )

    uploaded_file = request.files.get("file")

    if uploaded_file:
        FileService.upload(
            uploaded_file,
            current_user,
            folder,
        )

    return redirect(
        url_for(
            "folders.open",
            folder_id=folder.id,
        )
    )
