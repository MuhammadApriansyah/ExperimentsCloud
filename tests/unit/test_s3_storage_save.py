from io import BytesIO
from unittest.mock import Mock, patch

from app.storage.s3 import S3Storage


@patch("boto3.client")
def test_save_uploads_file(
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

        uploaded = Mock()

        uploaded.stream = BytesIO(b"hello world")

        storage.save(
            uploaded,
            "users/1/test.txt",
        )

        client.upload_fileobj.assert_called_once()
