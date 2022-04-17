from flask import jsonify, request

from . import api


@api.route('/products')
def get_products():
    page = request.args.get('page', 1, type=int)
    prod_per_page = request.args.get('per_page', 5, type=int)
    return jsonify({'page': page, 'per_page': prod_per_page})


@api.route('/products/<int:id>')
def get_product(id):
    user_ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    user_ip2 = request.environ.get('X-Real-IP', request.remote_addr)
    return jsonify({"id": id, 'ip': user_ip, 'id2': user_ip2})


@api.route('/cart')
def cart():
    id_cart = request.args.get('id_cart', None, type=int)

    if id_cart is None:
        return jsonify({"msg": "error_id_cart"}), 404

    prod_in_cart = [{'id': 1, "name": 'asd'}, {'id': 2, "name": "sad"}]
    return jsonify({"id_cart": id_cart, "products": [prod for prod in prod_in_cart]})
