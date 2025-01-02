from collections.abc import Sequence
from pathlib import Path
from typing import Any

import pytest

__all__ = (
    "get_yaml",
    "update_parser",
)

APP_NAME_TOKEN: str
CLI_NAME_TOKEN: str
IMPLEMENTATION_PACKAGE_NAME: str

def get_qualname(name: str) -> str: ...
def get_optname(name: str) -> str: ...
def _add_option(
    parser: pytest.Parser,
    group: pytest.OptionGroup,
    *,
    name: str,
    help_text: str,
    default: str | None = None,
    required: bool | None = True,
    choices: Sequence[str] | None = None,
) -> None: ...
def update_parser(parser: pytest.Parser) -> None: ...
def _get_fallback_category() -> str: ...
def _get_fallback_package_data_folder_start() -> str: ...
def _get_fallback_package_name() -> str: ...
def get_yaml(conf: pytest.Config, path_f: Path) -> None: ...
def _parse_option_value(val: Any) -> str | None: ...
def _get_arg_value(conf: pytest.Config, name: str, fallback: str | None) -> str: ...
