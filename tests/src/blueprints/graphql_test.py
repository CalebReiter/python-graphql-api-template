import pytest
from src.types.errors import FlaskErrorMessages

def test_can_http_get_graphql(client):
    response = client.get("/graphql")
    assert response.json["error"]["message"] == FlaskErrorMessages.NOT_FOUND
    assert response.status == "404 NOT FOUND"


@pytest.mark.parametrize("client", [(True)], indirect=["client"])
def test_can_http_get_graphql_debug_mode(client):
    response = client.get("/graphql")
    assert b"GraphQL Playground" in response.data
    assert response.status == "200 OK"


def test_can_http_post_graphql(client):
    response = client.post(
        "/graphql",
        json={
            "query": """query fetchAllTodos {
                todos {
                  success
                }
              }"""
        },
    )
    assert response.json == {"data": {"todos": {"success": True}}}
    assert response.status == "200 OK"
