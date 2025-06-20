from Xiao.core.dir import dirr
from Xiao.core.bot import app
from Xiao.core.bot import start_bot

from .logging import LOGGER

dirr()

__all__ = ["app", "start_bot"]