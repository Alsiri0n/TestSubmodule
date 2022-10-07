from flask import Blueprint,render_template

flform = Blueprint('flokoform', __name__, template_folder='templates', static_folder='static')


@flform.route('/')
def index():
    return render_template('flform/contact.html', title='Форма обратной связи')
