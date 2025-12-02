from flask import Blueprint, jsonify, request
from src.view.http_types.http_request import HttpRequest

from src.main.composer.user_register_composer import user_register_composer
from src.main.composer.login_creator_composer import login_creator_composer

user_routes_bp = Blueprint('user_routes', __name__)

@user_routes_bp.route('/user/register', methods=['POST'])
def registry_user():
  http_request = HttpRequest(body=request.json)
  http_response = user_register_composer().handle(http_request=http_request)
  return jsonify(http_response.body), http_response.status_code

@user_routes_bp.route('/user/login', methods=['POST'])
def create_login():
  http_request = HttpRequest(body=request.json)
  http_response = login_creator_composer().handle(http_request=http_request)
  return jsonify(http_response.body), http_response.status_code
  