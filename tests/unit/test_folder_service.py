from app.extensions import db

from app.models import (
    User,
    Folder,
)

from app.services import FolderService


def create_user():

    user = User(
        username="michi",
        email="michi@example.com",
    )

    user.set_password(
        "secret123"
    )

    db.session.add(user)
    db.session.commit()

    return user


def create_folder(user):

    folder = Folder(
        name="Documents",
        owner=user,
    )

    db.session.add(folder)
    db.session.commit()

    return folder


def test_create_folder(app):

    with app.app_context():

        user = create_user()

        folder = FolderService.create(
            "Documents",
            user,
        )

        assert folder.id is not None

        assert folder.name == "Documents"

        assert folder.owner_id == user.id


def test_list_root(app):

    with app.app_context():

        user = create_user()

        FolderService.create(
            "B",
            user,
        )

        FolderService.create(
            "A",
            user,
        )

        folders = FolderService.list_root(
            user,
        )

        assert len(folders) == 2

        assert folders[0].name == "A"

        assert folders[1].name == "B"


def test_get_user_folder(app):

    with app.app_context():

        user = create_user()

        folder = create_folder(
            user,
        )

        result = FolderService.get_user_folder(
            folder.id,
            user.id,
        )

        assert result == folder


def test_rename(app):

    with app.app_context():

        user = create_user()

        folder = create_folder(
            user,
        )

        renamed = FolderService.rename(
            folder,
            "Projects",
        )

        assert renamed.name == "Projects"

        refreshed = db.session.get(
            Folder,
            folder.id,
        )

        assert (
            refreshed.name
            == "Projects"
        )


def test_delete(app):

    with app.app_context():

        user = create_user()

        folder = create_folder(
            user,
        )

        FolderService.delete(
            folder,
        )

        assert Folder.query.count() == 0


def test_list_children(app):

    with app.app_context():

        user = create_user()

        parent = FolderService.create(
            "Documents",
            user,
        )

        FolderService.create(
            "Project A",
            user,
            parent,
        )

        FolderService.create(
            "Project B",
            user,
            parent,
        )

        children = FolderService.list_children(
            parent,
        )

        assert len(children) == 2

        assert children[0].name == "Project A"

        assert children[1].name == "Project B"


def test_list_children_empty(app):

    with app.app_context():

        user = create_user()

        parent = FolderService.create(
            "Documents",
            user,
        )

        children = FolderService.list_children(
            parent,
        )

        assert children == []


def test_get_parent(app):

    with app.app_context():

        user = create_user()

        parent = FolderService.create(
            "Documents",
            user,
        )

        child = FolderService.create(
            "Project A",
            user,
            parent,
        )

        result = FolderService.get_parent(
            child,
        )

        assert result == parent


def test_get_parent_root(app):

    with app.app_context():

        user = create_user()

        root = FolderService.create(
            "Documents",
            user,
        )

        assert (
            FolderService.get_parent(root)
            is None
        )


def test_build_path(app):

    with app.app_context():

        user = create_user()

        documents = FolderService.create(
            "Documents",
            user,
        )

        project = FolderService.create(
            "Project A",
            user,
            documents,
        )

        backend = FolderService.create(
            "Backend",
            user,
            project,
        )

        path = FolderService.build_path(
            backend,
        )

        assert [f.name for f in path] == [
            "Documents",
            "Project A",
            "Backend",
        ]


def test_build_path_root(app):

    with app.app_context():

        user = create_user()

        root = FolderService.create(
            "Documents",
            user,
        )

        path = FolderService.build_path(
            root,
        )

        assert [f.name for f in path] == [
            "Documents",
        ]
