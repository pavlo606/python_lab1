"""Logging"""
import logging

from Insects.exceptions_templates.invalid_mode_error import InvalidModeError

FORMAT = "[%(asctime)s - %(levelname)s %(name)s]: %(message)s"

def logged(exception, mode: str):
    """Decorator that logs exception to file or to console"""
    def _logged(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)

            except exception as exc:
                if mode == "file":
                    logging.basicConfig(filename="logs/insect.log",
                                        filemode='a', format=FORMAT)
                elif mode == "console":
                    logging.basicConfig(level=logging.ERROR, format=FORMAT)
                else:
                    raise InvalidModeError(f"\"{mode}\" is not a valid mode") from exc
                logger = logging.getLogger(__name__)
                logger.exception(exception.__name__)
        return inner
    return _logged
