from rest_framework.views import exception_handler


def generic_exception_handler(exc, context):
    handlers = {
        "ValidationError": _handle_validation_error,
        "Http404": _handle_not_found_error,
        "PermissionDenied": _handle_permission_error,
        "NotAuthenticated": _handle_auth_error,
    }

    response = exception_handler(exc, context)

    exception_class = exc.__class__.__name__
    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)


def _handle_validation_error(exc, context, response):
    return response


def _handle_not_found_error(exc, context, response):
    return {
        "error": "Requested URL not found"
    }


def _handle_permission_error(exc, context, response):
    return response


def _handle_auth_error(exc, context, response):
    return response
