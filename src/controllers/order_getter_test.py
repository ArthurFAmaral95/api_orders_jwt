from src.controllers.order_getter import OrderGetter
from src.models.repositories.order_repository import OrderRepository
from src.models.settings.db_connection_handler import db_connection_handler

class MockOrderRepository:
  def get_orders_by_user_id(self, user_id):
    return [(1, 'test order', '2025-10-10 06:52:57.791814-03:00'), (2, 'test order 2', '2025-10-10 06:56:49.791612-03:00'), (3, 'test order 2', '2025-10-16 06:16:43.293645-03:00'), (4, 'test order 2', '2025-10-16 06:18:01.628195-03:00')]
  
def test_get_orders():
  controller = OrderGetter(MockOrderRepository())

  response = controller.get_orders(user_id=1)
  
  assert response['type'] == 'Orders'
  assert response['count'] == 4
  assert isinstance(response['orders'], list)

# def test_integration_get_orders():
#   db_connection_handler.connect()
#   controller = OrderGetter(OrderRepository(conn=db_connection_handler.get_connection()))

#   response = controller.get_orders(user_id=2)

#   print()
#   print(response)