from unittest.mock import Mock
from unittest.mock import patch

import pytest
from botocore.exceptions import ClientError

from app.storage.s3 import S3Storage


@patch("boto3.client")
def test_open_returns_stream(
    boto_client_mock,
    app,
):
    client = Mock()

    body = Mock()

    client.get_object.return_value = {
        "Body": body,
    }

    boto_client_mock.return_value = client

    with app.app_context():
        app.config["AWS_ACCESS_KEY_ID"] = "access"
        app.config["AWS_SECRET_ACCESS_KEY"] = "secret"
        app.config["AWS_REGION"] = "ap-southeast-1"
        app.config["AWS_BUCKET"] = "bucket"

        storage = S3Storage()

        stream = storage.open(
            "users/1/file.txt",
        )

        assert stream is body


@patch("boto3.client")
def test_open_calls_get_object(
    boto_client_mock,
    app,
):
    client = Mock()

    client.get_object.return_value = {
        "Body": Mock(),
    }

    boto_client_mock.return_value = client

    with app.app_context():
        app.config["AWS_ACCESS_KEY_ID"] = "access"
        app.config["AWS_SECRET_ACCESS_KEY"] = "secret"
        app.config["AWS_REGION"] = "ap-southeast-1"
        app.config["AWS_BUCKET"] = "bucket"

        storage = S3Storage()

        storage.open(
            "users/1/file.txt",
        )

        client.get_object.assert_called_once_with(
            Bucket="bucket",
            Key="users/1/file.txt",
        )


@patch("boto3.client")
def test_open_reraises_client_error(
    boto_client_mock,
    app,
):
    client = Mock()

    client.get_object.side_effect = ClientError(
        {
            "Error": {
                "Code": "403",
            },
        },
        "GetObject",
    )

    boto_client_mock.return_value = client

    with app.app_context():
        app.config["AWS_ACCESS_KEY_ID"] = "access"
        app.config["AWS_SECRET_ACCESS_KEY"] = "secret"
        app.config["AWS_REGION"] = "ap-southeast-1"
        app.config["AWS_BUCKET"] = "bucket"

        storage = S3Storage()

        with pytest.raises(ClientError):
            storage.open(
                "users/1/file.txt",
            )
