from datetime import datetime
from slugify import slugify
from app.pages.models import PostTag
from app import db


class Post(db.Model):
    __tablename__ = 'pages_posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    slug = db.Column(db.String(128))
    categories = db.Column(db.Integer, db.ForeignKey('pages_categories.id'))
    content = db.Column(db.String)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.now)
    online = db.Column(db.Boolean)
    tags = db.relationship('Tag', secondary=PostTag, backref='pages_posts')


    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def __str__(self):
        return '%s : %s' % (self.id, self.title)

    def __repr__(self):
        return '<Page %r %r>' % (self.id, self.title)

    def generate_slug(self):
        self.slug = ''
        if self.title:
            self.slug = slugify(self.title)
