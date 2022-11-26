import pytest
from _pytest.fixtures import SubRequest
from flask.testing import FlaskClient
from graphql.language import OperationDefinitionNode
from graphql.type import GraphQLObjectType, GraphQLResolveInfo, GraphQLSchema

from src.router import app


@pytest.fixture()
def client(request: SubRequest) -> FlaskClient:
    """Configure test client.

    Args:
        request (SubRequest): SubRequest for handling fixture parameters.

    Returns:
        FlaskClient: The Test Client
    """
    debug = hasattr(request, "param") and request.param
    app.debug = debug
    return app.test_client()


@pytest.fixture()
def graphql_resolve_info() -> GraphQLResolveInfo:
    info = GraphQLResolveInfo(
        "field_name",
        [],
        GraphQLObjectType("query", {}),
        GraphQLObjectType("query", {}),
        "",
        GraphQLSchema(),
        {},
        None,
        OperationDefinitionNode(operation="query"),
        {},
        None,
        False,
    )
    return info
