import logging
import sys

from app.core.config import settings

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(settings.LOG_FORMAT)

handler.setFormatter(formatter)
logger = logging.getLogger("api")
logger.propagate = False

log_level = logging.getLevelName(settings.LOG_LEVEL)
logger.setLevel(log_level)
logger.addHandler(handler)
