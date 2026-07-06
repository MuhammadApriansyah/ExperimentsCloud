from unittest.mock import Mock
from unittest.mock import patch

from app.storage.s3 import S3Storage


@patch("boto3.client")
def test_constructor_creates_client(
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

        assert storage.client is client


@patch("boto3.client")
def test_constructor_reads_bucket(
    boto_client_mock,
    app,
):

    with app.app_context():

        app.config["AWS_ACCESS_KEY_ID"] = "access"

        app.config["AWS_SECRET_ACCESS_KEY"] = "secret"

        app.config["AWS_REGION"] = "ap-southeast-1"

        app.config["AWS_BUCKET"] = "bucket"

        storage = S3Storage()

        assert storage.bucket == "bucket"


@patch("boto3.client")
def test_constructor_passes_credentials(
    boto_client_mock,
    app,
):

    with app.app_context():

        app.config["AWS_ACCESS_KEY_ID"] = "my-access"

        app.config["AWS_SECRET_ACCESS_KEY"] = "my-secret"

        app.config["AWS_REGION"] = "eu-west-1"

        app.config["AWS_BUCKET"] = "bucket"

        S3Storage()

        boto_client_mock.assert_called_once_with(
            "s3",
            aws_access_key_id="my-access",
            aws_secret_access_key="my-secret",
            region_name="eu-west-1",
        )
