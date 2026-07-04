from app.extensions import db

from app.models import User


def create_user():

    user = User(
        username="michi",
        email="michi@example.com",
    )

    user.set_password("secret123")

    db.session.add(user)
    db.session.commit()

    return user


def login(client):

    create_user()

    return client.post(
        "/auth/login",
        data={
            "email": "michi@example.com",
            "password": "secret123",
        },
        follow_redirects=True,
    )


def test_folders_page_requires_login(client):

    response = client.get(
        "/folders/",
        follow_redirects=False,
    )

    assert response.status_code in (
        302,
        401,
    )


def test_folder_create_requires_login(client):

    response = client.get(
        "/folders/create",
        follow_redirects=False,
    )

    assert response.status_code in (
        302,
        401,
    )

def test_create_page(client):

    login(client)

    response = client.get(
        "/folders/create",
        follow_redirects=True,
    )

    assert response.status_code == 200

    assert b"Create Folder" in response.data


def test_create_folder_success(client):

    login(client)

    response = client.post(
        "/folders/create",
        data={
            "name": "Documents",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200

    assert b"Documents" in response.data

    assert (
        b"Folder created successfully."
        in response.data
    )

from app.models import Folder


def test_rename_page(client):

    login(client)

    with client.application.app_context():

        user = User.query.filter_by(
            email="michi@example.com",
        ).first()

        folder = Folder(
            name="Documents",
            owner=user,
        )

        db.session.add(folder)
        db.session.commit()

        folder_id = folder.id

    response = client.get(
        f"/folders/rename/{folder_id}",
        follow_redirects=True,
    )

    assert response.status_code == 200

    assert b"Rename Folder" in response.data


def test_rename_success(client):

    login(client)

    with client.application.app_context():

        user = User.query.filter_by(
            email="michi@example.com",
        ).first()

        folder = Folder(
            name="Documents",
            owner=user,
        )

        db.session.add(folder)
        db.session.commit()

        folder_id = folder.id

    response = client.post(
        f"/folders/rename/{folder_id}",
        data={
            "name": "Projects",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200

    assert b"Projects" in response.data


def test_rename_other_user_folder(client):

    login(client)

    with client.application.app_context():

        other = User(
            username="other",
            email="other@example.com",
        )

        other.set_password("secret123")

        db.session.add(other)
        db.session.commit()

        folder = Folder(
            name="Secret",
            owner=other,
        )

        db.session.add(folder)
        db.session.commit()

        folder_id = folder.id

    response = client.get(
        f"/folders/rename/{folder_id}",
    )

    assert response.status_code == 404


def test_delete_folder_success(client):

    login(client)

    with client.application.app_context():

        user = User.query.filter_by(
            email="michi@example.com",
        ).first()

        folder = Folder(
            name="Documents",
            owner=user,
        )

        db.session.add(folder)
        db.session.commit()

        folder_id = folder.id

    response = client.post(
        f"/folders/delete/{folder_id}",
        follow_redirects=True,
    )

    assert response.status_code == 200

    assert b"Documents" not in response.data


def test_delete_other_user_folder(client):

    login(client)

    with client.application.app_context():

        other = User(
            username="other",
            email="other@example.com",
        )

        other.set_password("secret123")

        db.session.add(other)
        db.session.commit()

        folder = Folder(
            name="Secret",
            owner=other,
        )

        db.session.add(folder)
        db.session.commit()

        folder_id = folder.id

    response = client.post(
        f"/folders/delete/{folder_id}",
    )

    assert response.status_code == 404


def test_open_folder(client):

    login(client)

    with client.application.app_context():

        user = User.query.filter_by(
            email="michi@example.com",
        ).first()

        parent = Folder(
            name="Documents",
            owner=user,
        )

        db.session.add(parent)
        db.session.commit()

        child = Folder(
            name="Project A",
            owner=user,
            parent=parent,
        )

        db.session.add(child)
        db.session.commit()

        folder_id = parent.id

    response = client.get(
        f"/folders/{folder_id}",
        follow_redirects=True,
    )

    assert response.status_code == 200

    assert b"Project A" in response.data


def test_open_other_user_folder(client):

    login(client)

    with client.application.app_context():

        other = User(
            username="other",
            email="other@example.com",
        )

        other.set_password("secret123")

        db.session.add(other)
        db.session.commit()

        folder = Folder(
            name="Secret",
            owner=other,
        )

        db.session.add(folder)
        db.session.commit()

        folder_id = folder.id

    response = client.get(
        f"/folders/{folder_id}",
    )

    assert response.status_code == 404


from unittest.mock import patch


@patch("app.folders.routes.render_template")
def test_open_folder_passes_path(
    render_template_mock,
    client,
):

    login(client)

    with client.application.app_context():

        user = User.query.filter_by(
            email="michi@example.com",
        ).first()

        parent = Folder(
            name="Documents",
            owner=user,
        )

        db.session.add(parent)

        db.session.commit()

        child = Folder(
            name="Project A",
            owner=user,
            parent=parent,
        )

        db.session.add(child)

        db.session.commit()

        folder_id = child.id

    client.get(
        f"/folders/{folder_id}",
    )

    _, kwargs = render_template_mock.call_args

    assert "path" in kwargs

    assert [f.name for f in kwargs["path"]] == [
        "Documents",
        "Project A",
    ]


def test_open_folder_shows_breadcrumb(client):

    login(client)

    with client.application.app_context():

        user = User.query.filter_by(
            email="michi@example.com",
        ).first()

        documents = Folder(
            name="Documents",
            owner=user,
        )

        db.session.add(documents)
        db.session.commit()

        project = Folder(
            name="Project A",
            owner=user,
            parent=documents,
        )

        db.session.add(project)
        db.session.commit()

        response = client.get(
            f"/folders/{project.id}",
            follow_redirects=True,
        )

    assert response.status_code == 200

    assert b"Documents" in response.data

    assert b"Project A" in response.data
