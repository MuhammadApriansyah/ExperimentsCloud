from flask import (
    render_template,
)

from app.errors import errors

from app.services.logging_service import (
    logger,
)

@errors.app_errorhandler(404)
def not_found(error):

    logger.warning(
        "404 | %s",
        error,
    )

    return (
        render_template(
            "errors/404.html"
        ),
        404,
    )


@errors.app_errorhandler(500)
def internal(error):

    logger.exception(
        "500 Internal Server Error"
    )

    return (
        render_template(
            "errors/500.html"
        ),
        500,
    )


@errors.app_errorhandler(Exception)
def unexpected(error):

    logger.exception(error)

    return (
        render_template(
            "errors/500.html"
        ),
        500,
    )
