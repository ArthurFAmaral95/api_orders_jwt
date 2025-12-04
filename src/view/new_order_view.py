from datetime import datetime
from src.controllers.new_order import NewOrderInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.view.interfaces.view_interface import ViewInterface
from src.errors.types.bad_request_error import HttpBadRequestError

class NewOrderView(ViewInterface):
  def __init__(self, controller: NewOrderInterface):
    self.__controller = controller

  def handle(self, http_resquest: HttpRequest) -> HttpResponse:
    description = http_resquest.body.get('description')
    user_id = http_resquest.params.get('user_id')
    order_date = datetime.now().astimezone()

    header_user_id = http_resquest.headers.get('uid')

    self.__validate_inputs(description=description, order_date=order_date, user_id=user_id, header_user_id=header_user_id)

    order_info = {
      'description': description,
      'order_date': order_date,
      'user_id': user_id
    }

    response = self.__controller.order(order_info=order_info)

    return HttpResponse(body={'data': response}, status_code=200)

  def __validate_inputs(self, description: any, order_date: any, user_id: any, header_user_id: any) -> None:
    if(
      not description
      or not order_date
      or not user_id
      or not isinstance(description, str)
      or (int(user_id) != int(header_user_id))
    ): raise HttpBadRequestError('Invalid input')