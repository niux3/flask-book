from datetime import datetime
from slugify import slugify
from app import db


class Page(db.Model):
    __tablename__ = 'pages_pages'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    slug = db.Column(db.String(128))
    content = db.Column(db.String)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    created = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.now)

    def __init__(self, *args, **kwargs):
        super(Page, self).__init__(*args, **kwargs)
        self.generate_slug()

    def __str__(self):
        return '%s : %s' % (self.id, self.title)

    def __repr__(self):
        return '<Page %r %r>' % (self.id, self.title)

    def generate_slug(self):
        self.slug = ''
        if self.title:
            self.slug = slugify(self.title)
