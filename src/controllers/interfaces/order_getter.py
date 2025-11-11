from abc import ABC, abstractmethod

class OrderGetterInterface(ABC):
  @abstractmethod
  def get_orders(self, user_id: int) -> dict: pass