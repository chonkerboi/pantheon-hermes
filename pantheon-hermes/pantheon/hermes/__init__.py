import asyncio

from .version import __version__
from . import fan
from . import command
from . import gpu
from . import nvidia
from . import power
from . import overclock

DISPLAY = 999
engine = asyncio.get_event_loop()

__all__ = ['__version__', 'fan', 'engine', 'command', 'gpu', 'nvidia', 'DISPLAY', 'power']
