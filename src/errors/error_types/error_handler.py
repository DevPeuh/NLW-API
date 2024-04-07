from src.http_types.http_response import HttpResponse
from .http_conflict import HttpConflictError
from .http_not_found import HttpNotFoundError

def handle_error(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpConflictError, HttpNotFoundError)):
        return HttpResponse(
            body={
                'errors': [{
                    'title': error.name,
                    'details': error.message,
                }]
            },
            status_code=error.status_code
        )
    
    return HttpResponse(
        body={

            'erros': [{
                'title': 'error',
                'details': str(error)
            }]
        }
    )