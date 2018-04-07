================================================================
django-curtains - Middleware for temporarily protecting projects
================================================================

.. image:: https://travis-ci.org/matthiask/django-curtains.svg?branch=master
    :target: https://travis-ci.org/matthiask/django-curtains


Usage
=====

- Install the module using ``pip install django-curtains``
- Add one of the included middleware to ``MIDDLEWARE``


``curtains.middleware.only_staff``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Only allows access to authenticated staff members. The
``ONLY_STAFF_EXEMPT`` setting (defaults to ``('/admin', 'accounts')``
allows excluding URLs from the middleware.


``curtains.middleware.basic_auth``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Requires basic authorization to access the site. The
``BASIC_AUTH_CREDENTIALS`` setting should be set to a list containing
the username and the password for basic authorization, e.g.
``BASIC_AUTH_CREDENTIALS = ['early', 'birds']``.
