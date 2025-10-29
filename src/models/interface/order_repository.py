from abc import ABC, abstractmethod

class OrderRepositoryInterface(ABC):
  @abstractmethod
  def new_order(self, description: str, order_date:str, user_id: str) -> None: pass

  @abstractmethod
  def get_orders_by_user_id(self, user_id: str) -> tuple: pass
  