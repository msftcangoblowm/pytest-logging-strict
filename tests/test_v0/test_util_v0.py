"""
.. moduleauthor:: Dave Faulkmore <https://mastodon.social/@msftcangoblowme>

Without coverage

.. code-block:: shell

   pytest --showlocals -vv tests/test_v0/test_util_v0.py

"""

from __future__ import annotations

import warnings
from fnmatch import fnmatch
from typing import cast

import pytest

from pytest_logging_strict.util import (
    _parse_option_value,
    get_optname,
    get_qualname,
    get_yaml_v0,
)


@pytest.mark.parametrize(
    (
        "yaml_package_name, package_data_folder_start, category, genre, "
        "flavor, version_no, return_type, warning_msg"
    ),
    (
        pytest.param(
            "logging_strict",
            "configs",
            "worker",
            "mp",
            "asz",
            "1",
            str,
            None,
            id="successful-query",
        ),
        pytest.param(
            "",
            "configs",
            "worker",
            "mp",
            "asz",
            "1",
            str,
            None,
            id="Has-sane-default-for-package-name",
        ),
        pytest.param(
            "logging_strict",
            "",
            "worker",
            "mp",
            "asz",
            "1",
            str,
            None,
            id="Has-sane-default-for-package_start_folder_name",
        ),
        pytest.param(
            "logassert",
            "configs",
            "worker",
            "mp",
            "asz",
            "1",
            None,
            "package_name * not installed. Before extracting package data, install the package into venv",
            id="ImportError",
        ),
        pytest.param(
            "logging_strict",
            "configs",
            "worker",
            "mp",
            "bob",
            "1",
            None,
            (
                "Within package *, starting from *, found *. Expected one. "
                "Is in this package? Is folder too specific? Try casting a wider net?"
            ),
            id="FileNotFoundError",
        ),
        pytest.param(
            "logging_strict",
            "bad_idea",
            "worker",
            "mp",
            "shared",
            "1",
            None,
            (
                "Within package *, starting from *, found *. Expected one. "
                "Adjust / narrow param, path_relative_package_dir"
            ),
            id="AssertionError",
        ),
        pytest.param(
            "logging-strict",
            "configs",
            "worker",
            "mp",
            "asz",
            "1",
            str,
            None,
            id="extract-issue",
        ),
    ),
)
def test_get_yaml_v0(
    yaml_package_name: str,
    package_data_folder_start: str,
    category: str,
    genre: str,
    flavor: str,
    version_no: str,
    return_type: type | None,
    warning_msg: str | None,
    pytester: pytest.Pytester,
    impl_version_no: str,
    request: "pytest.FixtureRequest",
) -> None:
    """Call pytest_addoption to test util module"""
    # pytest --showlocals -r a -vv --log-level INFO -k "test_get_yaml_v0" tests
    path_pytester = pytester.path  # noqa: F841
    abspath_tests_dir = request.path.parent.parent
    # prepare
    #    conftest.py
    conftest_text = abspath_tests_dir.joinpath("conftest.py").read_text()
    pytester.makeconftest(conftest_text)

    #    cli options
    args = [
        get_optname("impl_version_no"),
        impl_version_no,
        get_optname("yaml_package_name"),
        yaml_package_name,
        get_optname("package_data_folder_start"),
        package_data_folder_start,
        get_optname("category"),
        category,
        get_optname("genre"),
        genre,
        get_optname("flavor"),
        flavor,
        get_optname("version_no"),
        version_no,
    ]
    # Calls pytest_cmdline_parse which calls pytest_addoption
    # ns = conf.option
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter(action="ignore", category=UserWarning)
        conf = pytester.parseconfig(*args)
        val = conf.getoption(get_qualname("yaml_package_name"))
    parsed_val = _parse_option_value(val)
    parsed_val_expected = _parse_option_value(yaml_package_name)
    assert parsed_val == parsed_val_expected

    # No configuration file prepared
    # assert conf.getini(get_qualname("yaml_package_name")) == yaml_package_name
    pass

    # from path_f gets path_pytester folder
    path_f = path_pytester.joinpath("deleteme.logging.config.yaml")

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter(action="ignore", category=UserWarning)
        out_actual = get_yaml_v0(conf, path_f)
        if len(w) == 1:
            assert issubclass(w[-1].category, UserWarning)
            msg_actual = str(w[-1].message)
            if msg_actual is warning_msg is None:
                is_match = True
            else:
                str_msg_actual = cast("str", msg_actual)
                str_warning_msg = cast("str", warning_msg)
                is_match = fnmatch(str_msg_actual, str_warning_msg)
                assert is_match

    if return_type is None:
        assert out_actual is None
    elif return_type is str:
        assert isinstance(out_actual, return_type)
    else:  # pragma: no cover
        pass
