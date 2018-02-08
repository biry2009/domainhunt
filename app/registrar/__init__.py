from flask import Blueprint
registrar = Blueprint('registrar', __name__,)
from . import views