from functools import wraps
from django.http import HttpResponseForbidden

def my_decorator(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("Forbidden")
        return view_func(request, *args, **kwargs)
    return _wrapped_view
