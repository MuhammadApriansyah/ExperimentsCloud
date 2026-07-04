from datetime import datetime

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
        default=datetime.utcnow
    )

    owner = db.relationship(
        "User",
        back_populates="files"
    )

    def __repr__(self):
        return (
            f"<File {self.original_name}>"
        )
