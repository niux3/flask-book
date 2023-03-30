from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, ValidationError, SelectField
from wtforms.validators import InputRequired


class PageForm(FlaskForm):
    title = StringField('titre', validators=[InputRequired(message="ne doit pas être vide")])
    category = SelectField('catégorie', choices=(('', 'choisir une catégorie'), (1, 'blog'), (2, 'static')), validators=[InputRequired(message="ne doit pas être vide")])
    content = TextAreaField('contenu', validators=[InputRequired(message="ne doit pas être vide")])
    online = BooleanField('en ligne', default='1')

    # def validate(self):
    #     count = 0
    #     if 'pizza' in self.title.data:
    #         self.title.errors += (ValidationError("pas de pizza"),)
    #         count += 1
    #
    #     return count == 0
