"""Router for Officiate.io Backend API."""

from typing import Any, Dict, Tuple

import awsgi
from flask import Flask, jsonify
from flask.wrappers import Response

import src.blueprints as bp
from src._graphql import type_defs

app = Flask(__name__)


app.register_blueprint(bp.errors)
app.register_blueprint(bp.graphql)
app.config["type_defs"] = type_defs


@app.route("/")
def index() -> Tuple[Response, int]:
    """Index route.

    Returns:
        Response: 200 OK
    """
    return jsonify(message="OK"), 200


def lambda_handler(
    event: Dict[str, Any], context: Any
) -> Dict[str, Any]:  # pragma: no cover
    """Handle AWS Lambda Event.

    Args:
        event (Dict[str, Any]): AWS Lambda Event
        context (Any): AWS Lambda Context

    Returns:
        Dict[str, Any]: Response from the api
    """
    return awsgi.response(app, event, context, base64_content_types={"image/png"})


if __name__ == "__main__":  # pragma: no cover
    app.run(port=5000, debug=True)  # noqa: S201
