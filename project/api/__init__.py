from flask import Blueprint

api = Blueprint('api', __name__)

from . import auth
from . import product
from . import order
from . import user