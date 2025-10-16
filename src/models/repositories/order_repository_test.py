from datetime import datetime
from unittest.mock import Mock

from src.models.repositories.order_repository import OrderRepository
from src.models.settings.db_connection_handler import db_connection_handler

class MockCursor:
  def __init__(self):
    self.execute = Mock()
    self.fetchall = Mock()

class MockConnection:
  def __init__(self):
    self.cursor = Mock(return_value=MockCursor())
    self.commit = Mock()

def test_new_order():
  db_connection_handler.connect()
  conn = db_connection_handler.get_connection()
  repo = OrderRepository(conn)

  description = 'test order 2'
  order_date = datetime.now().astimezone()
  user_id = 1

  #repo.new_order(description=description, order_date=order_date, user_id=user_id)
  # orders = repo.get_orders_by_user_id(user_id=user_id)
  # print()
  # print(orders)

def test_unit_new_order():
  mock_connection = MockConnection()
  repo = OrderRepository(mock_connection)

  description = 'Unit order test'
  order_date = datetime.now().astimezone()
  user_id = 1

  repo.new_order(description=description, order_date=order_date, user_id=user_id)

  cursor = mock_connection.cursor.return_value

  assert 'INSERT INTO orders' in cursor.execute.call_args[0][0]
  assert '(description, order_date, user_id)' in cursor.execute.call_args[0][0]
  assert 'VALUES' in cursor.execute.call_args[0][0]
  assert cursor.execute.call_args[0][1] == (description, order_date, user_id)

  mock_connection.commit.assert_called_once()

def test_unit_get_orders_by_user_id():
  mock_connection = MockConnection()
  repo = OrderRepository(mock_connection)

  user_id = 1

  repo.get_orders_by_user_id(user_id=user_id)

  cursor = mock_connection.cursor.return_value

  assert 'SELECT id, description, order_date' in cursor.execute.call_args[0][0]
  assert 'FROM orders' in cursor.execute.call_args[0][0]
  assert 'WHERE user_id = ?' in cursor.execute.call_args[0][0]
  assert cursor.execute.call_args[0][1] == (user_id,)

  cursor.fetchall.assert_called_once()