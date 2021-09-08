{%- macro heading(text) -%}
{{text}}
{% for _ in text %}={% endfor %}
{%- endmacro -%}
{{ heading(cookiecutter.friendly_name) }}

|PyPI| |Status| |Python Version| |License|

|Read the Docs| |Tests| |Codecov|

|pre-commit|

.. |PyPI| image:: https://img.shields.io/pypi/v/{{cookiecutter.plugin_name}}.svg
   :target: https://pypi.org/project/{{cookiecutter.plugin_name}}/
   :alt: PyPI
.. |Status| image:: https://img.shields.io/pypi/status/{{cookiecutter.plugin_name}}.svg
   :target: https://pypi.org/project/{{cookiecutter.plugin_name}}/
   :alt: Status
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/{{cookiecutter.plugin_name}}
   :target: https://pypi.org/project/{{cookiecutter.plugin_name}}
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/{{cookiecutter.plugin_name}}
   :target: https://opensource.org/licenses/{{cookiecutter.license}}
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/{{cookiecutter.plugin_name}}/latest.svg?label=Read%20the%20Docs
   :target: https://{{cookiecutter.plugin_name}}.readthedocs.io/
   :alt: Read the documentation at https://{{cookiecutter.plugin_name}}.readthedocs.io/
.. |Tests| image:: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.plugin_name}}/workflows/Tests/badge.svg
   :target: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.plugin_name}}/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.plugin_name}}/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.plugin_name}}
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit


Features
--------

* TODO


Requirements
------------

* TODO


Installation
------------

You can install *{{cookiecutter.friendly_name}}* via pip_ from PyPI_:

.. code:: console

   $ pip install {{cookiecutter.plugin_name}}


Usage
-----

Please see the `Command-line Reference <Usage_>`_ for details.


Contributing
------------

Contributions are very welcome.
To learn more, see the `Contributor Guide`_.


License
-------

Distributed under the terms of the `{{cookiecutter.license.replace("-", " ")}} license`_,
*{{cookiecutter.friendly_name}}* is free and open source software.


Issues
------

If you encounter any problems,
please `file an issue`_ along with a detailed description.


Credits
-------

This project was generated from `@hemna`_'s `APRSD Plugin Python Cookiecutter`_ template.

.. _@cjolowicz: https://github.com/cjolowicz
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _{{cookiecutter.license.replace("-", " ")}} license: https://opensource.org/licenses/{{cookiecutter.license}}
.. _PyPI: https://pypi.org/
.. _APRSD Plugin Python Cookiecutter: https://github.com/hemna/cookiecutter-aprsd-plugin
.. _file an issue: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.plugin_name}}/issues
.. _pip: https://pip.pypa.io/
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
.. _Usage: https://{{cookiecutter.plugin_name}}.readthedocs.io/en/latest/usage.html
