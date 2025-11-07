from sqlite3 import Connection

from src.models.interface.order_repository import OrderRepositoryInterface

class OrderRepository(OrderRepositoryInterface):
  def __init__(self, conn: Connection) -> None:
    self.__conn = conn

  def new_order(self, description: str, order_date: str, user_id: int) -> None:
    cursor = self.__conn.cursor()
    cursor.execute(
      '''
      INSERT INTO orders
        (description, order_date, user_id)
      VALUES
        (?, ?, ?);
      ''', (description, order_date, user_id)
    )
    self.__conn.commit()
    
  def get_orders_by_user_id(self, user_id: int) -> list:
    cursor = self.__conn.cursor()
    cursor.execute(
      '''
      SELECT id, description, order_date
      FROM orders
      WHERE user_id = ?
      ''', (user_id,)
    )
    orders = cursor.fetchall()
    return orders
  