from flask import render_template
from app.pages import bp


@bp.route('/')
def index():
    ctx = {
            'books': 4,    
            'authors': 5,    
            'categories': 8,    
    }
    return render_template('pages/index.html', **ctx)

