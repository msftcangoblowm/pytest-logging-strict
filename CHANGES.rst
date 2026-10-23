.. this will be appended to README.rst

Changelog
=========

..

   Feature request
   .................

   - ``*.logging.config.yaml`` exported to ``/tmp`` when test run.
     Eventhough already **modified version** exists within ``~/.local/share/``

     **Reproduce**

     ``pyproject.toml``

     .. code-block:: text

        [tool.pytest.ini_options]
        logging_strict_yaml_package_name = 'sqa_cf'
        logging_strict_package_data_folder_start = 'configs'
        logging_strict_category = 'worker'
        logging_strict_genre = 'mp'
        logging_strict_flavor = 'sqacf'
        logging_strict_version_no = '1'

    ``tests/conftest.py``

    .. code-block:: text

       pytest_plugins = [
           "logging_strict",
           "has_logging_occurred",
           "sqa_cf",
       ]

     :code:`@pytest.mark.logging_package_name("sqa_cf")`

     ``mp_1_sqacf.worker.logging.config.yaml`` exists in ``~/.local/share/``
     run pytest copies to ``/tmp`` why? Already exists in ``~/.local/share/``

     .. code-block:: shell

        cd curatables
        . .venv/bin/activate
        pytest -vv --showlocals --log-level INFO -k "test_models_crud" tests

    Look in folders ``/tmp`` and ``~/.local/share/``

    Document situation so others can troubleshoot similar situation

   - `rst2html5 alternative <https://github.com/marianoguerra/rst2html5/>`_
     Not maintained package. Would require forking and maintaining
     In the interim, use docutils

   Known regressions
   ..................

   Commit items for NEXT VERSION
   ..............................

   - ci(testsuite.yml): GITHUB_ENV vars for OS and Python version
   - fix: virtualenv conflict with distlib tox packaging python-discovery
   - chore: drop py39 py310
   - ci: bump versions
   - tests: pytest.mark.parametrize decorator testcases use pytest.param

.. scriv-start-here

.. _changes_0-2-3:

Version 0.2.3 — 2025-05-20
--------------------------------

- fix(conftest): in clean environment pytest_report_header avoid import error
- tests: complete static typing
- chore: bump versions
- ci: bump versions

.. _changes_0-2-2:

Version 0.2.2 — 2025-04-09
--------------------------------

- chore: pep639 compliance
- chore: bump logging-strict version
- ci: bump dependency version

.. _changes_0-2-1:

Version 0.2.1 — 2025-03-23
--------------------------------

- tests: fix logging linesep same on Windows and posix
- feat: add fixture has_logging_occurred
- chore(pre-commit): add check typos
- chore: update wreck support
- ci: bump dependencies version

.. _changes_0-2-0:

Version 0.2.0 — 2025-01-19
--------------------------------

- feat: integrate logging-strict logging config registry API
- fix(requirements-dev): add nudge pin for package virtualenv to mitigate CVE-2024-53899
- ci(quality): build README.rst using rst2html5

.. _changes_0-1-0.post1:

Version 0.1.0.post1 — 2025-01-03
--------------------------------

- ci(test-coverage.yml): fix breaking change by codecov/codecov-action v5

.. _changes_0-1-0.post0:

Version 0.1.0.post0 — 2025-01-03
--------------------------------

- docs(README.rst): fix one link

.. _changes_0-1-0:

Version 0.1.0 — 2025-01-03
--------------------------

- fix(plugin): tempfile unlink ignore PermissionError on windows
- fix(tox.ini): target mypy wrong package name
- fix: after write flush tempfile or pypy will complain
- feat: pytest plugin for initializing logging
- chore: add pre-commit support
- chore: add Makefile
- chore: add tox support. format linting mypy pre-commit coverage wreck
- chore: add gh workflows

.. scriv-end-here
