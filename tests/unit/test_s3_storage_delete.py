from unittest.mock import Mock
from unittest.mock import patch

import pytest
from botocore.exceptions import ClientError

from app.storage.s3 import S3Storage


@patch("boto3.client")
def test_delete_calls_delete_object(
    boto_client_mock,
    app,
):
    client = Mock()
    boto_client_mock.return_value = client

    with app.app_context():
        app.config["AWS_ACCESS_KEY_ID"] = "access"
        app.config["AWS_SECRET_ACCESS_KEY"] = "secret"
        app.config["AWS_REGION"] = "ap-southeast-1"
        app.config["AWS_BUCKET"] = "bucket"

        storage = S3Storage()

        storage.delete("users/1/file.txt")

        client.delete_object.assert_called_once_with(
            Bucket="bucket",
            Key="users/1/file.txt",
        )


@patch("boto3.client")
def test_delete_returns_none(
    boto_client_mock,
    app,
):
    client = Mock()
    boto_client_mock.return_value = client

    with app.app_context():
        app.config["AWS_ACCESS_KEY_ID"] = "access"
        app.config["AWS_SECRET_ACCESS_KEY"] = "secret"
        app.config["AWS_REGION"] = "ap-southeast-1"
        app.config["AWS_BUCKET"] = "bucket"

        storage = S3Storage()

        assert storage.delete("users/1/file.txt") is None


@patch("boto3.client")
def test_delete_reraises_client_error(
    boto_client_mock,
    app,
):
    client = Mock()

    client.delete_object.side_effect = ClientError(
        {
            "Error": {
                "Code": "403",
            },
        },
        "DeleteObject",
    )

    boto_client_mock.return_value = client

    with app.app_context():
        app.config["AWS_ACCESS_KEY_ID"] = "access"
        app.config["AWS_SECRET_ACCESS_KEY"] = "secret"
        app.config["AWS_REGION"] = "ap-southeast-1"
        app.config["AWS_BUCKET"] = "bucket"

        storage = S3Storage()

        with pytest.raises(ClientError):
            storage.delete("users/1/file.txt")


@patch("boto3.client")
def test_delete_missing_object_is_not_error(
    boto_client_mock,
    app,
):
    client = Mock()

    client.delete_object.return_value = {}

    boto_client_mock.return_value = client

    with app.app_context():
        app.config["AWS_ACCESS_KEY_ID"] = "access"
        app.config["AWS_SECRET_ACCESS_KEY"] = "secret"
        app.config["AWS_REGION"] = "ap-southeast-1"
        app.config["AWS_BUCKET"] = "bucket"

        storage = S3Storage()

        storage.delete("users/1/missing.txt")
