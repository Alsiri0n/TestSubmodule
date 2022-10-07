"""
Test submodule working for Jenkins CI/CD
"""
from flask import Blueprint,render_template

flform = Blueprint('flokoform', __name__, template_folder='templates', static_folder='static')


@flform.route('/')
def index():
    """
    Test index page for submodule
    """
    return render_template('flform/contact.html', title='Форма обратной связи')
