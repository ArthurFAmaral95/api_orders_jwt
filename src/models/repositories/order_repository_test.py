from datetime import datetime

from src.models.repositories.order_repository import OrderRepository
from src.models.settings.db_connection_handler import db_connection_handler

def test_new_order():
  db_connection_handler.connect()
  conn = db_connection_handler.get_connection()
  repo = OrderRepository(conn)

  description = 'test order 2'
  order_date = datetime.now().astimezone()
  user_id = 1

  #repo.new_order(description=description, order_date=order_date, user_id=user_id)
  orders = repo.get_orders_by_user_id(user_id=user_id)
  print()
  print(orders)