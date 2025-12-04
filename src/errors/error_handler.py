from src.view.http_types.http_response import HttpResponse
from src.errors.types.bad_request_error import HttpBadRequestError
from src.errors.types.http_not_found import NotFoundError
from src.errors.types.unauthorized import HttpUnauthorizedError

def handle_error(error: Exception) -> HttpResponse:
  if isinstance(error, (HttpBadRequestError, HttpUnauthorizedError, NotFoundError)):
    return HttpResponse(
      body={
        'errors': [{
          'title': error.name,
          'detail': error.message
        }]
      },
      status_code=error.status_code
    )
  
  return HttpResponse(
    body={
      'errors': [{
        'title': 'Server Error',
        'detail': str(error)
      }]
    },
    status_code=500
  )