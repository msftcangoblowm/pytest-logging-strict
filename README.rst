pytest-logging-strict
======================

pytest fixture logging configured from packaged YAML

|  |kit| |license| |versions|
|  |test-status| |codecov| |quality-status|
|  |stars| |mastodon-msftcangoblowm|

.. PYVERSIONS

\* Python 3.9 through 3.13, PyPy

**New in 0.1.x**

initial release;

Why?
-----

Every single test, of interest, has boilerplate to setup the logging
configuration. Which is coming from a variable in a constants module.

In each and every package. That logging configuration is hardcoded.

``logging-strict`` package manages logging configurations as strictly
validated YAML files. ``pytest-logging-strict`` adds pytest integration
which includes an easy to use fixture.

The alternatives is pull a str or a dict from a constants module. Or
dealing with built-in pytest fixture, caplog.

With pytest integration:

- querying

  Once per pytest session. Query options are provided in
  ``pyproject.toml``. cli provided options override.

  Pulls the logging config YAML from logging-strict, but can pull from
  any installed package. Can submit your logging config YAML file to
  ``logging-strict``.

  Share your logging configuration. Have it accessible and available
  for all your packages, and as a bonus, everyone elses' packages.

- extracting

  Once per pytest session. Overrides logging-strict to force extracting
  into session scoped temp folder. After each session automagically removed.

- pytest fixture

  Use ``logging_strict`` fixture. Provides both the logger and list of
  all available loggers.

  So know which loggers are enabled besides only the main package logger

Installation
-------------

.. code:: shell

   python -m pip install pytest-logging-strict


Configuration
--------------

In ``conftest.py``

.. code:: shell

   pytest_plugins = ["logging_strict"]

In ``pyproject.toml``

Customize the query. If not, the default is taken from ``logging-strict`` package.

.. code:: shell

    [tool.pytest.ini_options]
    logging_strict_yaml_package_name = 'logging_strict'
    logging_strict_package_data_folder_start = 'configs'
    logging_strict_category = 'worker'
    logging_strict_genre = 'mp'
    logging_strict_flavor = 'asz'
    logging_strict_version_no = '1'

and/or cli

.. code:: shell

   pytest --showlocals -vv --logging-strict-yaml-package-name = 'logging_strict' \
   --logging-strict-package-data-folder-start = 'configs' \
   --logging-strict-category = 'worker' \
   --logging-strict-genre = 'mp' \
   --logging-strict-flavor = 'asz' \
   --logging-strict-version-no = '1' tests

The cli overrides ``pyproject.toml`` settings.

Usage
------

Minimalistic example
"""""""""""""""""""""

pytest marker sends param ``package name`` to the fixture.
Creates the main logger instance. While still having access to
all possible loggers defined in the logger config YAML file. e.g. ``root``
and ``asyncio``.

.. code:: text

   import pytest

   @pytest.mark.logging_package_name("my_package_name")
   def test_fcn(logging_strict):
       t_two = logging_strict()
       if t_two is not None:
           logger, lst_loggers = t_two
           logger.info("Hello World!")

The pytest marker communicates ur package name to logging_strict fixture.
Which then initiates the main logger instance.

Full example
"""""""""""""

.. code:: text

   import logging
   from logging_strict.tech_niques import captureLogs
   import pytest

   @pytest.mark.logging_package_name("my_package_name")
   def test_fcn(logging_strict):
       t_two = logging_strict()
       if t_two is None:
           logger_name_actual == "root"
           fcn = logger.error
       else:
           assert isinstance(t_two, tuple)
           logger, lst_loggers = t_two
           logger_name_actual = logger.name
           logger_level_name_actual = logging.getLevelName(logger.level)

           msg = "Hello World!"

           # log message was logged and can confirm
           with captureLogs(
               logger_name_actual,
               level=logger_level_name_actual,
           ) as cm:
               fcn(msg)
           out = cm.output
           is_found = False
           for msg_full in out:
               if msg_full.endswith(msg):
                   is_found = True
           assert is_found

Batteries included
-------------------

**textual console apps**

.. code:: shell

   pytest --showlocals -vv --logging-strict-yaml-package-name = 'logging_strict' \
   --logging-strict-package-data-folder-start = 'configs' \
   --logging-strict-category = 'app' \
   --logging-strict-genre = 'textual' \
   --logging-strict-flavor = 'asz' \
   --logging-strict-version-no = '1' tests

**multiprocess worker** -- default

.. code:: shell

   pytest --showlocals -vv --logging-strict-yaml-package-name = 'logging_strict' \
   --logging-strict-package-data-folder-start = 'configs' \
   --logging-strict-category = 'worker' \
   --logging-strict-genre = 'mp' \
   --logging-strict-flavor = 'asz' \
   --logging-strict-version-no = '1' tests

Please submit your logging configuration for review and curation to
make available to everyone.

In the meantime or if not in the mood to share

.. code:: shell

   pytest --showlocals -vv --logging-strict-yaml-package-name = 'zope.interface' \
   --logging-strict-package-data-folder-start = 'data' \
   --logging-strict-category = 'worker' \
   --logging-strict-genre = 'mp' \
   --logging-strict-flavor = 'mine' \
   --logging-strict-version-no = '1' tests

The package data file would be stored as:

``data/mp_1_mine.worker.logging.config.yaml``

The flavor, e.g. ``mine``, should be alphanumeric no whitespace nor underscores.
e.g. ``justonebigblob``

Milestones
-----------

- Simplify querying

  `logging-strict#4 <https://github.com/msftcangoblowm/logging-strict/issues/4>`_
  will add support for a config TOML file. Which will contain logging config YAML records.

  Then the file naming convention will be dropped.

  The config TOML file is placed at the package base folder. And is the reference point
  to advertise which logging config YAML files are in the package.

- classifier

  pypi.org allows searching by classifiers. So will be easier for everyone
  to identify which packages offer logging config YAML files

License
--------

aGPLv3+ `[full text] <https://github.com/msftcangoblowm/logging-strict/blob/master/LICENSE.txt>`_

Collaborators
--------------

Note *there is no code of conduct*. Will **adapt to survive** any mean
tweets or dodgy behavior.

Can collaborate by:

ACTUALLY DO SOMETHING ... ANYTHING

- use ``pytest-logging-strict`` in your own packages' tests
- peer review and criticism. Make me cry, beg for leniency, and have
  no other recourse than to appeal to whats left of your humanity
- request features
- submit issues
- submit PRs
- follow on mastodon. Dropping messages to **say hello** or share offensive memes
- translate the docs into other languages
- leave a github star on repos you like
- write distribute and market articles to raise awareness

ASK FOR HELP

- ask for eyeballs to review your repo
- request for support

FOSS FUNDING

- apply force and coersion to take your monero or litecoin

- fund travel to come out to speak at tech conferences (currently residing in West Japan)

- Mr. Money McBags printer goes Brrrrr. Get assistance towards identifying
  package maintainers in need of funding

ASK FOR ABUSE

- Throw shade, negativity, and FUD at everything and anything. Do it!
  Will publically shame you into put your money where your mouth is.

- pointless rambling and noise that leads no where. Will play spot the
  pattern and respond with unpleasent truths, or worse, offensive memes

- Threaten to be useful or hold higher standing. e.g. recruiters or NPOs/NGOs

- suggest a code of conduct. Ewwwww! That's just down right mean

- suggest a license written by a drunkard

.. |test-status| image:: https://github.com/msftcangoblowm/pytest-logging-strict/actions/workflows/testsuite.yml/badge.svg?branch=master&event=push
    :target: https://github.com/msftcangoblowm/pytest-logging-strict/actions/workflows/testsuite.yml
    :alt: Test suite status
.. |quality-status| image:: https://github.com/msftcangoblowm/pytest-logging-strict/actions/workflows/quality.yml/badge.svg?branch=master&event=push
    :target: https://github.com/msftcangoblowm/pytest-logging-strict/actions/workflows/quality.yml
    :alt: Quality check status
.. |kit| image:: https://img.shields.io/pypi/v/pytest-logging-strict
    :target: https://pypi.org/project/pytest-logging-strict/
    :alt: PyPI status
.. |versions| image:: https://img.shields.io/pypi/pyversions/pytest-logging-strict.svg?logo=python&logoColor=FBE072
    :target: https://pypi.org/project/pytest-logging-strict/
    :alt: Python versions supported
.. |license| image:: https://img.shields.io/github/license/msftcangoblowm/pytest-logging-strict
    :target: https://pypi.org/project/pytest-logging-strict/blob/master/LICENSE.txt
    :alt: License
.. |stars| image:: https://img.shields.io/github/stars/msftcangoblowm/pytest-logging-strict.svg?logo=github
    :target: https://github.com/msftcangoblowm/pytest-logging-strict/stargazers
    :alt: GitHub stars
.. |mastodon-msftcangoblowm| image:: https://img.shields.io/mastodon/follow/112019041247183249
    :target: https://mastodon.social/@msftcangoblowme
    :alt: msftcangoblowme on Mastodon
.. |codecov| image:: https://codecov.io/gh/msftcangoblowm/pytest-logging-strict/graph/badge.svg?token=3aE90WoGKg
    :target: https://codecov.io/gh/msftcangoblowm/pytest-logging-strict
    :alt: pytest-logging-strict coverage percentage
