import pytest
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.view.login_creator_view import LoginCreatorView

class MockController:
  def create(self, username, password):
    return {'alguma': 'coisa'}

def test_handle_login_creator():
  body = {
    'username': 'test_username',
    'password': 'test_password'
  }

  request = HttpRequest(body=body)

  view = LoginCreatorView(controller=MockController())

  response = view.handle(http_request=request)

  assert isinstance(response, HttpResponse)
  assert response.body == {'data': {'alguma': 'coisa'}}
  assert response.status_code == 200

def test_handle_login_creator_with_error():
  body = {
    'username': 'test_username'
  }

  request = HttpRequest(body=body)

  view = LoginCreatorView(controller=MockController())


  with pytest.raises(Exception):
    view.handle(http_request=request)
