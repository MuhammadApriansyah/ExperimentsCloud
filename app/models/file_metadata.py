from app.extensions import db


class FileMetadata(db.Model):
    __tablename__ = "file_metadata"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    file_id = db.Column(
        db.Integer,
        db.ForeignKey("files.id"),
        nullable=False,
        unique=True,
    )

    checksum = db.Column(
        db.String(64),
        nullable=True,
    )

    image_width = db.Column(
        db.Integer,
        nullable=True,
    )

    image_height = db.Column(
        db.Integer,
        nullable=True,
    )

    duration = db.Column(
        db.Integer,
        nullable=True,
    )

    page_count = db.Column(
        db.Integer,
        nullable=True,
    )

    indexed = db.Column(
        db.Boolean,
        nullable=False,
        default=False,
    )

    preview_available = db.Column(
        db.Boolean,
        nullable=False,
        default=False,
    )

    thumbnail_available = db.Column(
        db.Boolean,
        nullable=False,
        default=False,
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
    )

    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now(),
    )

    file = db.relationship(
        "File",
        back_populates="file_metadata"
    )

    def __repr__(self):
        return (
            f"<FileMetadata file_id={self.file_id}>"
        )
