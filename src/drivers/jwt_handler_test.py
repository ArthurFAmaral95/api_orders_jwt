from src.drivers.jwt_handler import JwtHandler

def test_jwt_handler():
  jwt_handler = JwtHandler()
  body = {
    'user_id': 1,
    'username': 'usuario teste'
  }

  token = jwt_handler.create_jwt_token(body=body)
  token_informations = jwt_handler.decode_jwt_token(token=token)

  assert token is not None
  assert isinstance(token, str)
  assert token_informations['user_id'] == body['user_id']
  assert token_informations['username'] == body['username']