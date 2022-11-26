"""Queries for Todo schema."""
from typing import Any, Dict

from ariadne import convert_kwargs_to_snake_case
from graphql.type import GraphQLResolveInfo

from src._graphql import query
from src.types.graphql import GraphQLUtils


@query.field("todos")
def resolve_todos(_: Any, info: GraphQLResolveInfo) -> Dict[str, Any]:
    """Resolve list of todos.

    Args:
        _ (Any): Data from parent resolver.
        info (GraphQLResolveInfo): Context for field and query.

    Returns:
        Dict[str, Any]: TodosResult
    """
    return {"success": True, "todos": []}


@query.field("todo")
@convert_kwargs_to_snake_case
def resolve_todo(_: Any, info: GraphQLResolveInfo, todo_id: int) -> Dict[str, Any]:
    """Resolve todo.

    Args:
        _ (Any): Data from parent resolver.
        info (GraphQLResolveInfo): Context for field and query.
        todo_id (int): ID of Todo to get.

    Returns:
        Dict[str, Any]: TodoResult
    """
    utils = GraphQLUtils(info=info)
    projection_fields = utils.get_projection("todo.todo")
    todo = {"id": 2, "completed": True, "description": "abc", "due_date": "2022-11-20"}
    todo = {k: v for k, v in todo.items() if k in projection_fields}
    return {"success": True, "todo": todo}
