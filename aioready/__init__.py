from typing import NamedTuple, Literal

from .database_enum import DatabaseType
from .database import (Connection, Database)
from .errors import *
from .utils import *

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int

__version__ = "1.0.0"
version_info: VersionInfo = VersionInfo(major=1, minor=0, micro=0, releaselevel='alpha', serial=0)