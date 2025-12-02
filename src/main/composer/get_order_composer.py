from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.order_repository import OrderRepository
from src.controllers.order_getter import OrderGetter
from src.view.get_order_view import GetOrderView

def get_order_composer():
  conn = db_connection_handler.get_connection()
  model = OrderRepository(conn=conn)
  controller = OrderGetter(order_repository=model)
  view = GetOrderView(controller=controller)

  return view
