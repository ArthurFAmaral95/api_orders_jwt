import pytest
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.view.get_order_view import GetOrderView

class MockController:
  def get_orders(self, user_id):
    return {
      'type': 'Orders',
      'count': 2,
      'orders': 'test orders'
    }
  
def test_handle_get_orders():
  params = {
    'user_id': 1
  }

  request = HttpRequest(params=params)
  view = GetOrderView(controller=MockController())

  response = view.handle(http_request=request)

  assert isinstance(response, HttpResponse)
  assert 'data' in response.body
  assert response.status_code == 200

def test_handle_get_order_with_error():
  params = {
    'user': 1
  }

  request = HttpRequest(params=params)
  view = GetOrderView(controller=MockController())

  with pytest.raises(Exception):
    view.handle(http_request=request)