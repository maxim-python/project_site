from app import app
from flask import render_template, current_app

from app.module.models import Metal_schingle

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Max'}
    return render_template('index.html', title='Каталог', user=user)


@app.route('/metallocherepica')
def catalog():
    tittle = "Кровмастер"
    product = Metal_schingle.query.all()
    return render_template('metallocherepica.html', page_tittle =  tittle, text = product)