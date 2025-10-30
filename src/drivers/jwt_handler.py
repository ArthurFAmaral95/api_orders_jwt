import jwt
from datetime import datetime, timedelta

class JwtHandler:
  def create_jwt_token(self, body: dict = {}) -> str:
    token = jwt.encode(
      payload={
        'exp': datetime.now().astimezone() + timedelta(hours=1),
        **body
      },
      key='minhachave',
      algorithm='HS256'
    )
    return token
  
  def decode_jwt_token(self, token: str) -> dict:
    token_information = jwt.decode(
      token,
      key='minhachave',
      algorithms='HS256'
    )
    return token_information
  