import boto3

from flask import current_app

from app.storage.backend import StorageBackend

from botocore.exceptions import ClientError

from app.storage.key_builder import StorageKeyBuilder


class S3Storage(StorageBackend):

    def __init__(self):

        self.bucket = current_app.config["AWS_BUCKET"]

        self.client = boto3.client(
            "s3",
            aws_access_key_id=current_app.config[
                "AWS_ACCESS_KEY_ID"
            ],
            aws_secret_access_key=current_app.config[
                "AWS_SECRET_ACCESS_KEY"
            ],
            region_name=current_app.config[
                "AWS_REGION"
            ],
        )

    def object_key(
        self,
        user_id: int,
        stored_name: str,
    ):
        raise NotImplementedError

    def save(
        self,
        uploaded_file,
        destination,
    ):
        self.client.upload_fileobj(
            uploaded_file.stream,
            self.bucket,
            destination,
        )

    def exists(
        self,
        path,
    ):
        try:
            self.client.head_object(
                Bucket=self.bucket,
                Key=path,
            )

            return True

        except ClientError as error:

            code = error.response["Error"]["Code"]

            if code in (
                "404",
                "NoSuchKey",
            ):
                return False

            raise

    def delete(
        self,
        path,
    ):
        self.client.delete_object(
            Bucket=self.bucket,
            Key=path,
        )

    def open(
        self,
        path,
    ):
        response = self.client.get_object(
            Bucket=self.bucket,
            Key=path,
        )

        return response["Body"]

    def key(
        self,
        user_id,
        stored_name,
    ):
        return StorageKeyBuilder.user_file(
            user_id,
            stored_name,
        )


    def resolve(self, key):
        return key
