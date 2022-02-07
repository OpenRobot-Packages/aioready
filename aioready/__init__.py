import typing
from typing import NamedTuple, Literal

# thank you dpy for this
# https://github.com/Rapptz/discord.py/blob/master/discord/__init__.py#L21

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int

version = "1.0.0"
version_info: VersionInfo = VersionInfo(major=1, minor=0, micro=0, releaselevel='alpha', serial=0)