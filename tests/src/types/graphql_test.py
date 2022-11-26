import pytest
from graphql.type import GraphQLObjectType, GraphQLOutputType, GraphQLResolveInfo

from src.types.errors import GraphQLUtilsErrorMessages
from src.types.graphql import GraphQLUtils


def test_can_GraphQLUtils_init():
    utils = GraphQLUtils()
    assert utils.info is None


def test_can_GraphQLUtils_init_with_info(graphql_resolve_info):
    utils = GraphQLUtils(info=graphql_resolve_info)
    assert utils.info == graphql_resolve_info


def test_can_GraphQLUtils_get_projection_raise_no_info():
    utils = GraphQLUtils()
    with pytest.raises(
        ValueError,
        match=GraphQLUtilsErrorMessages.CANNOT_GET_PROJECTION,
    ):
        utils.get_projection(["a", "b", "c"])


def test_can_GraphQLUtils_get_projection_raise_no_path(graphql_resolve_info):
    utils = GraphQLUtils(info=graphql_resolve_info)
    with pytest.raises(
        ValueError,
        match=GraphQLUtilsErrorMessages.escaped_message(
            "projection_not_found", ["a"], ["a", "b", "c"]
        ),
    ):
        utils.get_projection(["a", "b", "c"])


@pytest.mark.parametrize(
    ("camel_case", "snake_case", "keep_acronyms"),
    [
        ("", "", False),
        ("abc", "abc", False),
        ("aBc", "a_bc", False),
        ("aBc", "a_bc", True),
        ("graphQL", "graph_ql", True),
        ("GraphQL", "graph_ql", True),
        ("graphQL", "graph_q_l", False),
        ("httpGraphQLAPI", "http_graph_ql_api", True),
        ("httpOrHTTPS", "http_or_https", True),
    ],
)
def test_can_GraphQLUtils_camel_case_to_snake_case(
    camel_case: str, snake_case: str, keep_acronyms: bool
):
    utils = GraphQLUtils()
    assert (
        utils.camel_case_to_snake_case(camel_case, keep_acronyms=keep_acronyms)
        == snake_case
    )
