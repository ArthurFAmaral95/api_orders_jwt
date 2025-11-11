from abc import ABC, abstractmethod

class NewOrderInterface(ABC):
  @abstractmethod
  def order(self, order_info: dict) -> dict: pass