import base64

from django.conf import settings
from django.http import HttpResponse


def parse_basic_authorization(value):
    try:
        method, auth = value.split(" ", 1)
        if method.lower() == "basic":
            return base64.b64decode(auth).decode("latin-1").split(":", 1)
    except Exception:
        pass
    return None


def basic_auth(get_response):
    CREDENTIALS = list(settings.BASIC_AUTH_CREDENTIALS)

    def middleware(request):
        header = request.META.get("HTTP_AUTHORIZATION")
        if header and parse_basic_authorization(header) == CREDENTIALS:
            return get_response(request)

        response = HttpResponse()
        response.status_code = 401
        response["WWW-Authenticate"] = 'Basic realm="please"'
        return response

    return middleware
