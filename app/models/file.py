from datetime import UTC, datetime

from app.extensions import db


class File(db.Model):

    __tablename__ = "files"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    owner_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    original_name = db.Column(
        db.String(255),
        nullable=False
    )

    stored_name = db.Column(
        db.String(255),
        unique=True,
        nullable=False
    )

    file_extension = db.Column(
        db.String(20),
        nullable=False
    )

    mime_type = db.Column(
        db.String(100),
        nullable=False
    )

    file_size = db.Column(
        db.BigInteger,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(UTC)
    )

    owner = db.relationship(
        "User",
        back_populates="files"
    )

    folder = db.relationship(
        "Folder",
        back_populates="files",
    )

    def __repr__(self):
        return (
            f"<File {self.original_name}>"
        )

    folder_id = db.Column(
        db.Integer,
        db.ForeignKey("folders.id"),
        nullable=True,
     )


