from pprint import pprint
from flask import render_template, request, flash, redirect, url_for
from app.pages import bp
from app.pages.models import Post
from app.pages.forms import PageForm
from app import db


@bp.route('/')
def index():
    ctx = {
        'books': 4,
        'authors': 5,
        'categories': 8,
    }
    return render_template('pages/index.html', **ctx)


@bp.route('/ajouter-page', methods=['GET', 'POST'])
def add():
    form = PageForm(request.form)
    if request.method == 'POST' and form.validate():
        data = {
            'title': form.title.data,
            'content': form.content.data,
            'online': 1 if form.online.data == True else 0,
        }
        new_post = Post(**data)
        db.session.add(new_post)
        db.session.commit()
        flash("creation page effectuée", "success")
        return redirect(url_for('pages.index'))
    ctx = {
        'form': form
    }
    return render_template('pages/add.html', **ctx)
