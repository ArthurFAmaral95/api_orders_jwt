from flask import Blueprint, jsonify

user_routes_bp = Blueprint('user_routes', __name__)

@user_routes_bp.route('/', methods=['GET'])
def hello():
  return jsonify({'hello': 'arthur'}), 200