from flask import Blueprint, jsonify, request
from src.view.http_types.http_request import HttpRequest

from src.main.composer.new_order_composer import new_order_composer
from src.main.composer.get_order_composer import get_order_composer
from src.main.middleware.auth_jwt import auth_jwt_verify

order_routes_bp = Blueprint('order_routes', __name__)

@order_routes_bp.route('/order/new_order/<user_id>', methods=['POST'])
def place_order(user_id):
  token_information = auth_jwt_verify()
  http_request = HttpRequest(
    body=request.json, 
    params={'user_id': user_id},
    token_infos=token_information,
    headers=request.headers
    )
  http_response = new_order_composer().handle(http_resquest=http_request)
  return jsonify(http_response.body), http_response.status_code

@order_routes_bp.route('/order/get_orders/<user_id>', methods=['GET'])
def get_orders(user_id):
  token_information = auth_jwt_verify()
  http_request = HttpRequest(
    params={'user_id': user_id},
    token_infos=token_information,
    headers=request.headers
    )
  http_response = get_order_composer().handle(http_request=http_request)
  return jsonify(http_response.body), http_response.status_code
