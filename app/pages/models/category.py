from app import db


class Category(db.Model):
    __tablename__ = 'pages_categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    posts = db.relationship('Post', backref="pages_categories")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<{__class__.__name__} "{self.name}">'