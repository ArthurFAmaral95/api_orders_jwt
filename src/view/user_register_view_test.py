import pytest
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.view.user_register_view import UserRegisterView

class MockController:
  def registry(self, username, password):
    return {'alguma': 'coisa'}
  

def test_handle_user_register():
  body = {
    'username': 'test_username',
    'password': 'test_password'
  }

  request = HttpRequest(body=body)

  mock_controller = MockController()
  view = UserRegisterView(controller=mock_controller)

  response = view.handle(http_request=request)

  assert isinstance(response, HttpResponse)
  assert response.body == {'data': {'alguma': 'coisa'}}
  assert response.status_code == 201
  

def test_handle_user_register_with_validation_error():
  body = {
    'password': 'test_password'
  }

  mock_controller = MockController()
  view = UserRegisterView(controller=mock_controller)

  request = HttpRequest(body=body)

  with pytest.raises(Exception):
    view.handle(http_request=request)
    