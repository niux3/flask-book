from app import db


class Tag(db.Model):
    __tablename__ = 'pages_tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Tag "{self.name}">'
