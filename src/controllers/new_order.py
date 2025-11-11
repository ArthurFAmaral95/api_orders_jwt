from src.models.interface.order_repository import OrderRepositoryInterface
from src.controllers.interfaces.new_order import NewOrderInterface

class NewOrder(NewOrderInterface):
  def __init__(self, order_repository: OrderRepositoryInterface):
    self.__order_repository = order_repository

  def order(self, order_info: dict) -> dict:
    description = order_info['description']
    order_date = order_info['order_date']
    user_id = order_info['user_id']

    self.__place_order(description=description, order_date=order_date, user_id=user_id)
    return self.__format_response(order_info=order_info)

  def __place_order(self, description: str, order_date: str, user_id: int) -> None:
    self.__order_repository.new_order(description=description, order_date=order_date, user_id=user_id)

  def __format_response(self, order_info: dict) -> dict:
    return {
      'type': 'Order',
      'count': 1,
      'details': order_info
    }