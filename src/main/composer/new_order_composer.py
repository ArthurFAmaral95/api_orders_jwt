from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.order_repository import OrderRepository
from src.controllers.new_order import NewOrder
from src.view.new_order_view import NewOrderView

def new_order_composer():
  conn = db_connection_handler.get_connection()
  model = OrderRepository(conn=conn)
  controller = NewOrder(order_repository=model)
  view = NewOrderView(controller=controller)

  return view
