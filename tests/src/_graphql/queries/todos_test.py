def test_can_resolve_todos(client):
    response = client.post(
        "/graphql",
        json={
            "query": """query fetchAllTodos {
              todos {
                success
                todos {
                  id
                  description
                }
              }
            }"""
        },
    )
    assert response.json == {"data": {"todos": {"success": True, "todos": []}}}
    assert response.status == "200 OK"


def test_can_resolve_todo(client):
    response = client.post(
        "/graphql",
        json={
            "query": """query fetchTodo {
              todo(todoId:1) {
                success
                todo {
                  id
                  completed
                  description
                  dueDate
                }
              }
            }"""
        },
    )
    assert response.json == {
        "data": {
            "todo": {
                "success": True,
                "todo": {
                    "id": "2",
                    "completed": True,
                    "description": "abc",
                    "dueDate": "2022-11-20",
                },
            }
        }
    }
    assert response.status == "200 OK"
