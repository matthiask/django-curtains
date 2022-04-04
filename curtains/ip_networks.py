import ipaddress
import re

from django.conf import settings
from django.http import HttpResponse


IP_NETWORKS = [
    ipaddress.ip_network(spec)
    for spec in getattr(settings, "IP_NETWORKS", ["127.0.0.0/8"])
]

BLOCKED_PAGE = """
<!DOCTYPE html>
<html>
<body>
<h1>Unexpected IP address</h1>
<p>Your IP %s is not in the allowlist, sorry.</p>
</body>
</html>
"""


def visitor_ip_address(request):
    x_forwarded_for = request.headers.get("X-Forwarded-For")

    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def ip_networks_only(get_response):
    def middleware(request):
        if exempt := getattr(settings, "IP_NETWORKS_EXEMPT", None):
            if re.match(exempt, request.path):
                return get_response(request)

        ip = ipaddress.ip_address(visitor_ip_address(request))
        if any(ip in network for network in IP_NETWORKS):
            return get_response(request)
        return HttpResponse(BLOCKED_PAGE % ip, content_type="text/html", status=403)

    return middleware
