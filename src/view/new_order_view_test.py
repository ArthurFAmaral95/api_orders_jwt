import pytest
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.view.new_order_view import NewOrderView

class MockController:
  def order(self, order_info):
    return {'info': order_info}
  
def test_handle_new_order():
  body = {
    'description': 'test_description'
  }

  params = {
    'user_id': 1
  }

  request = HttpRequest(body=body, params=params)

  view = NewOrderView(controller=MockController())

  response = view.handle(http_resquest=request)

  assert isinstance(response, HttpResponse)
  assert 'data' in response.body
  assert response.status_code == 200

def test_handle_new_order_with_validation_error():
  body = {
    'description': ''
  }

  params = {
    'user_id': 1
  }

  request = HttpRequest(body=body, params=params)

  view = NewOrderView(controller=MockController())

  with pytest.raises(Exception):
    view.handle(http_resquest=request)
