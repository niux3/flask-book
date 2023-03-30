from app import db

PostTag = db.Table(
    'pages_post_tag',
    db.Column('posts_id', db.Integer, db.ForeignKey('pages_posts.id')),
    db.Column('tags_id', db.Integer, db.ForeignKey('pages_tags.id'))
)