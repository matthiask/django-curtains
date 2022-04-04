import re

from django.conf import settings
from django.http import HttpResponse


def convert_list_to_re(exempt):
    if isinstance(exempt, (tuple, list)):
        return "|".join("^%s" % re.escape(path) for path in exempt)
    return exempt


ONLY_STAFF_PAGE = """
<!DOCTYPE html>
<html>
<head lang="en">
  <meta charset="UTF-8">
  <meta name="robots" content="noindex,nofollow">
  <title>Only Staff Allowed</title>
  <style>
    body {
      text-align: center;}
    h1 {
      font-size: 50px; text-align: center }
    span[frown] {
      transform: rotate(90deg); display:inline-block; color: #bbb; }
    body {
      font: Georgia, Times, serif; color: #999;
      text-shadow: 2px 2px 2px rgba(200, 200, 200, 0.5); }
    ::-moz-selection{
      background:#4ff7fd; color:#111; }
    ::selection {
      background:#4ff7fd; color:#111; }
    article {
      display:block; text-align: left; width: 500px; margin: 0 auto; }
    a {
      color: rgb(36, 109, 56); text-decoration:none; }
    a:hover {
      color: rgb(96, 73, 141);
      text-shadow: 2px 2px 2px rgba(36, 109, 56, 0.5); }
  </style>
</head>
<body>
<article>
  <h1>Only Staff Allowed <span frown>:(</span></h1>
  <div>
    <p>Sorry, but we cannot show you this page right now. Please
    authenticate.</p>
    <p><a href="/admin/login/" target="_blank">Log in to the admin
    panel</a></p>
  </div>
</article>
</body>
</html>
"""


def _only_staff_exempt():
    return convert_list_to_re(
        getattr(settings, "ONLY_STAFF_EXEMPT", r"^/admin|^/accounts")
    )


def only_staff(get_response):
    def middleware(request):
        if re.match(_only_staff_exempt(), request.path):
            return get_response(request)
        elif not request.user.is_staff:
            return HttpResponse(ONLY_STAFF_PAGE, status=403)

        return get_response(request)

    return middleware
