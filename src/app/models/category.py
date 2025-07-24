from src.app.extensions import db


class Category(db.Model):  # type: ignore
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    products = db.relationship(
        "Product", backref="category", lazy=True, cascade="all, delete"
    )
