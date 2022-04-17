import os

from flask import make_response, request, jsonify, render_template, current_app
from flask_login import current_user
from werkzeug.utils import secure_filename
from . import api


# @api.route('/userava')
# def userava():
#     # img = current_user.getAvatar(app)
#     if not img:
#         return ""
#
#     h = make_response(img)
#     h.headers['Content-Type'] = 'image/png'
#     return h


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in current_app.config['ALLOWED_EXTENSIONS']


@api.route('/upload', methods=["POST"])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            return jsonify({'filename': filename})

    return jsonify({'msg': 'error'})
