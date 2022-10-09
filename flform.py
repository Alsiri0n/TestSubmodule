"""
Test submodule working for Jenkins CI/CD
"""
from flask import Blueprint,render_template,request,flash

flform = Blueprint('flokoform', __name__, template_folder='templates', static_folder='static')


@flform.route('/', methods=["GET", "POST"])
def index():
    """
    Test index page for submodule
    """
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено', category="success")
        else:
            flash('Ошибка отправки', category="error")
    return render_template('flform/contact.html', title='Форма обратной связи')
