from datetime import datetime
from src. controllers.new_order import NewOrder

class MockOrderRepository:
  def __init__(self):
    self.registry_use_attributes = {}

  def new_order(self, description, order_date, user_id):
    self.registry_use_attributes['description'] = description
    self.registry_use_attributes['order_date'] = order_date
    self.registry_use_attributes['user_id'] = user_id

def test_new_order():
  repository = MockOrderRepository()
  controller = NewOrder(order_repository=repository)

  order_info = {
    'description': 'unit test order',
    'order_date': datetime.now().astimezone(),
    'user_id': 1
  }

  response = controller.order(order_info=order_info)

  assert response['type'] == 'Order'

  assert repository.registry_use_attributes['description'] == order_info['description']
  assert repository.registry_use_attributes['order_date'] == order_info['order_date']
  assert repository.registry_use_attributes['user_id'] == order_info['user_id']
  