import logging
from pathlib import Path

from app.services.logging_service import (
    APP_LOG,
    ERROR_LOG,
    get_logger,
    logger,
)


def test_get_logger_returns_singleton():

    first = get_logger()
    second = get_logger()

    assert first is second


def test_logger_name():

    assert logger.name == "ExperimentsCloud"


def test_logger_level():

    assert logger.level == logging.INFO


def test_logger_has_required_handlers():

    assert any(
        isinstance(handler, logging.FileHandler)
        and Path(handler.baseFilename) == APP_LOG.resolve()
        for handler in logger.handlers
    )

    assert any(
        isinstance(handler, logging.FileHandler)
        and Path(handler.baseFilename) == ERROR_LOG.resolve()
        for handler in logger.handlers
    )

    assert any(
        type(handler) is logging.StreamHandler
        for handler in logger.handlers
    )


def test_console_handler():

    assert any(
        type(handler) is logging.StreamHandler
        for handler in logger.handlers
    )


def test_logger_propagation_disabled():

    assert logger.propagate is False
