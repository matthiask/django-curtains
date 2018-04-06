================================================================
django-curtains - Middleware for temporarily protecting projects
================================================================

Version |release|

Usage
=====

- Install the module using ``pip install django-curtains``
- Add one of the included middleware to ``MIDDLEWARE``

``curtains.middleware.only_staff``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Only allows access to authenticated staff members.


``curtains.middleware.basic_auth``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Requires basic authorization to access the site.


- `Github <https://github.com/matthiask/django-curtains/>`_
