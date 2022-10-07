from flask import Blueprint

flform = Blueprint('flokoform', __name__, template_folder='templates', static_folder='static')


@flform.route('/')
def index():
    return 'flokoform'
