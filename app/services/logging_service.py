import logging
from pathlib import Path


LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

APP_LOG = LOG_DIR / "app.log"
ERROR_LOG = LOG_DIR / "error.log"

APP_LOG.touch(exist_ok=True)
ERROR_LOG.touch(exist_ok=True)


def get_logger():
    logger = logging.getLogger("ExperimentsCloud")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    app_handler = logging.FileHandler(
        APP_LOG,
        encoding="utf-8",
    )
    app_handler.setLevel(logging.INFO)
    app_handler.setFormatter(formatter)

    error_handler = logging.FileHandler(
        ERROR_LOG,
        encoding="utf-8",
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logger.addHandler(app_handler)
    logger.addHandler(error_handler)
    logger.addHandler(console_handler)

    return logger


logger = get_logger()

logging.getLogger("werkzeug").disabled = True
logging.getLogger("werkzeug").propagate = False
logging.getLogger("flask.app").propagate = False
