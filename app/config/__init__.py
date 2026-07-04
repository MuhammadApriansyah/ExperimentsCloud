import os

from .development import DevelopmentConfig
from .production import ProductionConfig
from .testing import TestingConfig


CONFIG_MAP = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}


def get_config():

    environment = os.getenv(
        "FLASK_ENV",
        "development",
    ).lower()

    return CONFIG_MAP.get(
        environment,
        DevelopmentConfig,
    )
