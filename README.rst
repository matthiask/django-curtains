================================================================
django-curtains - Middleware for temporarily protecting projects
================================================================

.. image:: https://github.com/matthiask/django-curtains/workflows/Tests/badge.svg
    :target: https://github.com/matthiask/django-curtains/
    :alt: CI Status


Usage
=====

- Install the module using ``pip install django-curtains``
- Add one of the included middleware to ``MIDDLEWARE``


``curtains.middleware.only_staff``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Only allows access to authenticated staff members. The ``ONLY_STAFF_EXEMPT``
setting (defaults to ``r"^/admin|^/accounts"``) allows excluding URLs from the
middleware.


``curtains.middleware.basic_auth``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Requires basic authorization to access the site. The ``BASIC_AUTH_CREDENTIALS``
setting should be set to a list containing the username and the password for
basic authorization, e.g. ``BASIC_AUTH_CREDENTIALS = ['early', 'birds']``.
``BASIC_AUTH_EXEMPT`` can be set to a regex of paths to exempt from the
authorization requirement.


``curtains.middleware.ip_networks_only``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Requires a list of networks in the ``IP_NETWORKS`` setting. The default is
``127.0.0.0/8``. The ``IP_NETWORKS_EXEMPT`` setting exists.
