from flask import jsonify, make_response, current_app, request
# from flask_jwt_extended import create_access_token, create_refresh_token, unset_jwt_cookies, jwt_required, \
#     get_jwt_identity, set_access_cookies
from flask_login import login_user, login_required, current_user, logout_user
from flask_wtf.csrf import generate_csrf, validate_csrf
from werkzeug.utils import redirect

from . import api
from ..email import send_email
from ..forms import RegistrationForm
from ..models import *


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


@api.route("/register", methods=['POST', 'GET'])
def auth_register():
    try:
        if request.method == 'POST':

            # Получаем данные из запроса
            userJSON = request.get_json(force=True)

            # Передаем данные в форму для валидации
            form = RegistrationForm(data=userJSON)

            print(request.headers['X-CSRFToken'])
            print(form.Meta.csrf)
            print(validate_csrf(request.headers['X-CSRFToken']))

            # Провемеряем данные на валидность
            if not form.validate():
                return jsonify({'msg': 'Incorrect data', "errors": form.errors}), 400





            # Check form, duplicate,
            # Add to db
            # Send email

            if Users.get_user_by_email(email):
                return jsonify({'msg': "Users with such an email already exists"}), 409

            # # Создание и добавление профиля пользователя
            # profile = Profile(form.username)
            # db.session.add(profile)
            # db.session.flush()
            #
            # # Создание и добавление токена пользователя
            # refresh_token = create_refresh_token(form.email)
            # ip_address = request.remote_addr
            # token = Token(ip_address=ip_address, refresh_token=refresh_token)
            # db.session.add(token)
            # db.session.flush()
            #
            # # Создание модели пользователя и добавление его в БД
            # user = Users(email=form.email, password=form.password,
            #             profile_id=profile.id,
            #             token_id=token.id)
            # db.session.add(user)
            # db.session.commit()

            # # Получение ссылки активации
            # activationLink = user.activationLink

            # sendMessageToEmail(email=user.email, link=activationLink)
            # send_email(to=user.email, actLink=activationLink)

            return jsonify({'msg': 'Registration success'}), 200

        elif request.method == 'GET':
            # Generate CSRF token for forms
            csrf_token = generate_csrf()
            response = make_response({"csrf_token": csrf_token})
            response.headers.add_header('X-CSRFToken', csrf_token)
            response.set_cookie('X-CSRFToken', csrf_token)
            return response, 200
    except Exception as ex:
        print(ex)
        db.session.rollback()
        return ({"msg": "Internal Server Error"}), 500


@api.route("/login", methods=['POST'])
def auth_login():
    try:
        email = request.json['email']
        password = request.json['password']

        print(email, password)

        # Getting user
        user = User.query.filter_by(email=email).first()

        if user is not None and user.verify_password(password):
            login_user(user, False)
            response = jsonify({"msg": 'success'})
            return response, 200

        #
        # if not user.isActivated:
        #     return jsonify({"msg": 'Users account has not been activated. You need to activate your account!'}), 400

        return jsonify({"msg": "Invalid login or password"}), 400

    except Exception as ex:
        print(ex)
        return ({"msg": "Internal Server Error"}), 500


@api.route("/test", methods=['POST', 'GET'])
@login_required
def test():
    user = current_user.id

    return jsonify({"asd": "sad", 'user': user})


@api.route("/logout", methods=['POST'])
@login_required
def user_logout():
    logout_user()
    response = jsonify({'msg': 'logout is success'})
    return response, 200
