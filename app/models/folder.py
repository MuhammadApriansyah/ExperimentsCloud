from datetime import UTC, datetime

from app.extensions import db


class Folder(db.Model):

    __tablename__ = "folders"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    name = db.Column(
        db.String(255),
        nullable=False,
    )

    owner_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
    )

    parent_id = db.Column(
        db.Integer,
        db.ForeignKey("folders.id"),
        nullable=True,
    )

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(UTC),
        nullable=False,
    )

    owner = db.relationship(
        "User",
        back_populates="folders",
    )

    parent = db.relationship(
        "Folder",
        remote_side=[id],
        back_populates="children",
    )

    children = db.relationship(
        "Folder",
        back_populates="parent",
        cascade="all, delete-orphan",
    )

    files = db.relationship(
        "File",
        back_populates="folder",
    )

    def __repr__(self):

        return (
            f"<Folder {self.name}>"
        )
