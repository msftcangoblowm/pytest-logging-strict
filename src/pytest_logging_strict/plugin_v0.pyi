from dataclasses import dataclass
from pathlib import Path
from typing import Self

import pytest

# https://github.com/pytest-dev/pytest-xdist/issues/1121
from xdist.workermanage import WorkerController  # type: ignore

@dataclass(frozen=True)  # compat python < 3.10 (kw_only=True)
class LSConfigStash:
    logging_strict_config_yaml_path: Path

    @classmethod
    def from_serialized(cls, serialized: str | Path) -> Self: ...
    def remove(self) -> None: ...
    def serialized(self) -> str: ...

stash_key: dict[str, pytest.StashKey[LSConfigStash]]

class LoggingStrictv0XdistControllerPlugin:
    def pytest_configure_node(self, node: WorkerController) -> None: ...

def _configure(
    config: pytest.Config,
    xdist_worker_: dict[str, WorkerController | pytest.Config],
) -> None: ...

class LoggingStrictv0ControllerPlugin:
    def pytest_unconfigure(self, config: pytest.Config) -> None: ...
