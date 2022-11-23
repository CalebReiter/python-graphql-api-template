def test_can_run_index(client):
    response = client.get("/")
    assert response.json["message"] == "OK"
    assert response.status == "200 OK"
