from flask import request, jsonify

from . import api


@api.route('/order')
def get_order():
    order_id = request.args.get('id', None, type=int)

    if order_id is None:
        return jsonify({'msg': "error"}), 404

    return jsonify({"id": order_id, "customer": {"name": "Sasha", 'email': 'sasgar@mail.ru'}})
