from flask import jsonify, make_response, current_app
# from flask_jwt_extended import create_access_token, create_refresh_token, unset_jwt_cookies, jwt_required, \
#     get_jwt_identity, set_access_cookies
from flask_login import login_user, login_required
from werkzeug.utils import redirect

from ..email import send_email

from ..models import *
from . import api, controller


# @api.route('/test', methods=['POST'])
# def test():
#     user = User.query.filter_by(email='sasharepin2016@mail.ru').first()
#
#     if user is not None and user.verify_password('qwer123'):
#         login_user(user, False)
#
#     return jsonify({'success': 'true'})
#
#
# @api.route('/auth', methods=['GET'])
#
# def auth():
#     return jsonify({'isAuth': 'true'})


@api.route("/register", methods=['POST'])
def auth_register():
    return controller.register()


@api.route("/login", methods=['POST'])
def auth_login():
    return controller.login()


@api.route("/logout", methods=['POST'])
@login_required
def user_logout():
    return controller.logout()

