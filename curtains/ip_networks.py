import ipaddress

from django.conf import settings
from django.http import HttpResponse


IP_NETWORKS = [ipaddress.ip_network(spec) for spec in settings.IP_NETWORKS]

BLOCKED_PAGE = """
<!DOCTYPE html>
<html>
<body>
<h1>IP blocked, sorry</h1>
</body>
</html>
"""


def visitor_ip_address(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")

    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def ip_networks_only(get_response):
    def middleware(request):
        ip = ipaddress.ip_address(visitor_ip_address(request))
        if any(ip in network for network in IP_NETWORKS):
            return get_response(request)
        return HttpResponse(BLOCKED_PAGE, content_type="text/html", status=403)

    return middleware
