from src.models.interface.order_repository import OrderRepositoryInterface
from src.controllers.interfaces.order_getter import OrderGetterInterface

class OrderGetter(OrderGetterInterface):
  def __init__(self, order_repository: OrderRepositoryInterface):
    self.__order_repository = order_repository

  def get_orders(self, user_id: int) -> dict:
    orders = self.__fetch_orders_in_db(user_id=user_id)
    return self.__format_response(orders=orders)

  def __fetch_orders_in_db(self, user_id: int) -> list:
    orders = self.__order_repository.get_orders_by_user_id(user_id=user_id)
    return orders
  
  def __format_response(self, orders: list) -> dict:
    return {
      'type': 'Orders',
      'count': len(orders),
      'orders': orders
    }