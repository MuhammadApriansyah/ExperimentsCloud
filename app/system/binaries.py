import os
import shutil

from flask import current_app


class BinaryNotFoundError(RuntimeError):
    """Raised when an external binary cannot be located."""


def find_binary(config_key: str, executable: str) -> str:
    """
    Resolve an executable using the following priority:

    1. Flask configuration
    2. Environment variable
    3. System PATH
    """

    config_value = current_app.config.get(config_key)

    if config_value:
        return config_value

    env_value = os.getenv(config_key)

    if env_value:
        return env_value

    discovered = shutil.which(executable)

    if discovered:
        return discovered

    raise BinaryNotFoundError(
        f"Unable to locate '{executable}'. "
        f"Configure '{config_key}' or install the executable."
    )
