Change log
==========

`Next version`_
~~~~~~~~~~~~~~~

.. _Next version: https://github.com/matthiask/django-curtains/compare/0.6...main


`0.6`_ (2022-04-04)
~~~~~~~~~~~~~~~~~~~

.. _0.6: https://github.com/matthiask/django-curtains/compare/0.5...0.6

- Modernized the package, dropped Python<3.8 and Django<3.2.
- Added pre-commit.
- Added ``BASIC_AUTH_EXEMPT`` and ``IP_NETWORKS_EXEMPT`` settings.


`0.5`_ (2021-03-03)
~~~~~~~~~~~~~~~~~~~

.. _0.5: https://github.com/matthiask/django-curtains/compare/0.4...0.5

- Dropped Python<3.6 and Django<2.2.
- Verified support for Django 3.x and Python 3.8 and 3.9.
- Switched to using a declarative setup.
- Switched from Travis CI to GitHub actions.
- Allowed specifying a regex for ``ONLY_STAFF_EXEMPT``.
- Renamed the main branch to ``main``.


`0.4`_ (2019-06-13)
~~~~~~~~~~~~~~~~~~~

- Added a middleware which allows whitelisting IP networks.
- Dropped Python 2 compatibility.


`0.3`_ (2018-09-12)
~~~~~~~~~~~~~~~~~~~

- Added Django 2.1 to the build matrix.
- Reformatted the Python code using black.
- Basic authorization: Fail earlier if there are no credentials.


`0.2`_ (2018-04-06)
~~~~~~~~~~~~~~~~~~~

- Renamed the project to django-curtains, and added a basic
  authorization-using middleware.


`0.1`_ (2018-02-26)
~~~~~~~~~~~~~~~~~~~

- Initial public version.

.. _0.1: https://github.com/matthiask/django-curtains/commit/89bb93c5cdba
.. _0.2: https://github.com/matthiask/django-curtains/compare/0.1...0.2
.. _0.3: https://github.com/matthiask/django-curtains/compare/0.2...0.3
.. _0.4: https://github.com/matthiask/django-curtains/compare/0.3...0.4
