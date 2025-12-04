from src.controllers.interfaces.order_getter import OrderGetterInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.view.interfaces.view_interface import ViewInterface

class GetOrderView(ViewInterface):
  def __init__(self, controller: OrderGetterInterface) -> None:
    self.__controller = controller

  def handle(self, http_request: HttpRequest) -> HttpResponse:
    user_id = http_request.params.get('user_id')
    header_user_id = http_request.headers.get('uid')

    self.__validate_inputs(user_id=user_id, header_user_id=header_user_id)

    response = self.__controller.get_orders(user_id=user_id)

    return HttpResponse(body={'data': response}, status_code=200)


  def __validate_inputs(self, user_id: any, header_user_id: any) -> None:
    if not user_id or (int(user_id) != int(header_user_id)):
      raise Exception('Invalid Input')