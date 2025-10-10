from sqlite3 import Connection

class OrderRepository:
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
    