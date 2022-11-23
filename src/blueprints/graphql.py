"""Blueprints for graphql."""

from typing import Tuple

from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from flask import Blueprint, current_app, jsonify, request
from flask.wrappers import Response

from src._graphql.schema import schema
from src.types.errors import ErrorResponse

graphql = Blueprint("graphql", __name__)


@graphql.route("/graphql", methods=["GET"])
def graphql_playground() -> Tuple[str, int]:
    """Route for GraphQL Playground if we are in debug mode.

    Raises:
        ErrorResponse: if debug mode is not on

    Returns:
        Tuple[str, int]: graphql playground
    """
    if current_app.debug:
        return PLAYGROUND_HTML, 200
    raise ErrorResponse("NOT FOUND", status_code=404)


@graphql.route("/graphql", methods=["POST"])
def graphql_server() -> Tuple[Response, int]:
    """Route for GraphQL requests.

    Returns:
        Tuple[Response, int]: graphql result
    """
    data = request.get_json()
    success, result = graphql_sync(
        schema, data, context_value=request, debug=current_app.debug
    )
    status = 200 if success else 400
    return jsonify(result), status
