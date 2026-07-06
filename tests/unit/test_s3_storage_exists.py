from unittest.mock import Mock, patch

import pytest
from botocore.exceptions import ClientError

from app.storage.s3 import S3Storage


@patch("boto3.client")
def test_exists_returns_true(
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

        assert storage.exists(
            "users/1/file.txt"
        ) is True

        client.head_object.assert_called_once_with(
            Bucket="bucket",
            Key="users/1/file.txt",
        )


@patch("boto3.client")
def test_exists_returns_false_when_missing(
    boto_client_mock,
    app,
):
    client = Mock()

    client.head_object.side_effect = ClientError(
        {
            "Error": {
                "Code": "404",
            },
        },
        "HeadObject",
    )

    boto_client_mock.return_value = client

    with app.app_context():

        app.config["AWS_ACCESS_KEY_ID"] = "access"
        app.config["AWS_SECRET_ACCESS_KEY"] = "secret"
        app.config["AWS_REGION"] = "ap-southeast-1"
        app.config["AWS_BUCKET"] = "bucket"

        storage = S3Storage()

        assert storage.exists(
            "users/1/file.txt"
        ) is False


@patch("boto3.client")
def test_exists_reraises_other_errors(
    boto_client_mock,
    app,
):
    client = Mock()

    client.head_object.side_effect = ClientError(
        {
            "Error": {
                "Code": "403",
            },
        },
        "HeadObject",
    )

    boto_client_mock.return_value = client

    with app.app_context():

        app.config["AWS_ACCESS_KEY_ID"] = "access"
        app.config["AWS_SECRET_ACCESS_KEY"] = "secret"
        app.config["AWS_REGION"] = "ap-southeast-1"
        app.config["AWS_BUCKET"] = "bucket"

        storage = S3Storage()

        with pytest.raises(ClientError):
            storage.exists(
                "users/1/file.txt"
            )
