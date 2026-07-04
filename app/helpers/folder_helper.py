from flask import abort

from app.services import FolderService


def get_owned_folder_or_404(
    folder_id,
    user_id,
):

    folder = FolderService.get_user_folder(
        folder_id,
        user_id,
    )

    if folder is None:
        abort(404)

    return folder
