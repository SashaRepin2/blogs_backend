from flask import request, jsonify, url_for, make_response
# from flask_jwt_extended import create_refresh_token, create_access_token
from flask_login import logout_user, login_user
from werkzeug.utils import redirect

from project import db

from project.models import User


def register():
    try:
        print(register)

        # Check form, duplicate,
        # Add to db
        # Send email

        # if Users.get_user_by_email(email):
        #     return jsonify({'msg': "Users with such an email already exists"}), 409
        #
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

    except Exception as ex:
        print(ex)
        db.session.rollback()
        return ({"msg": "Internal Server Error"}), 500


def login():
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


def logout():
    logout_user()
    response = jsonify({'msg': 'logout is success'})
    return response, 200
