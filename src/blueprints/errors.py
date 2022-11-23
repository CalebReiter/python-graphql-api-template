"""Blueprints for Error Handling."""

from typing import Tuple

from flask import Blueprint, jsonify
from flask.wrappers import Response

from src.types.errors import ErrorResponse

errors = Blueprint("errors", __name__)


def error_route(status: int) -> None:
    """Jsonify error status code.

    Args:
        status (int): Status code to handle.
    """

    @errors.app_errorhandler(status)
    def _error(e: Exception) -> Tuple[Response, int]:
        return jsonify(error=str(e)), status


@errors.app_errorhandler(ErrorResponse)
def error(e: ErrorResponse) -> Tuple[Response, int]:
    """Jsonfiy error response.

    Args:
        e (ErrorResponse): The error to respond with.

    Returns:
        Tuple[Response, int]: the error response

    """
    return jsonify(error=e.to_dict()), e.status_code


for status in [500, 400, 404]:
    error_route(status)
