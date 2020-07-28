from functools import wraps
from django.http.response import JsonResponse
from books.models import Session

def is_logged(fn):
    @wraps(fn)
    def loggin_wrapper(obj, request, *args, **kwargs):
        access_token = request.headers.get('Authorization', None)
        session = Session.objects(access_token=access_token)
        if session and session.count() == 1:
            return fn(obj, request, *args, **kwargs)
        else:
            return JsonResponse({'msg':'Token expired'})

    return loggin_wrapper
