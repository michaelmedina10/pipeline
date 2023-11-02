import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

debug_handler = logging.FileHandler("debug.log")
debug_handler_fmt = '%(asctime)s - %(levelname)s [%(filename)s:%(funcName)s:%(lineno)d] - %(message)s'
debug_handler.setFormatter(logging.Formatter(debug_handler_fmt))
debug_handler.setLevel(logging.DEBUG)

logger.addHandler(debug_handler)
