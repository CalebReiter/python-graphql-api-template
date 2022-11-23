def test_can_http_handle_error(client):
    response = client.post("/graphql", data="1234")
    assert response.json == {
        "error": (
            "400 Bad Request: "
            "The browser (or proxy) sent a request "
            "that this server could not understand."
        )
    }
    assert response.status == "400 BAD REQUEST"
