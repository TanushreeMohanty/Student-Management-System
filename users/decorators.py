from django.http import HttpResponseForbidden

def role_required(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("You are not allowed to view this page")
        return wrapper_func
    return decorator
