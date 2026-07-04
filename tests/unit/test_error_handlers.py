from app.errors.handlers import (
    not_found,
    internal,
    unexpected,
)


def test_not_found(app):

    with app.test_request_context():

        response, status = not_found(
            Exception("Not Found")
        )

        assert status == 404

        assert "404" in response


def test_internal(app):

    with app.test_request_context():

        response, status = internal(
            Exception("Boom")
        )

        assert status == 500

        assert "500" in response


def test_unexpected(app):

    with app.test_request_context():

        response, status = unexpected(
            Exception("Unexpected")
        )

        assert status == 500

        assert "500" in response
