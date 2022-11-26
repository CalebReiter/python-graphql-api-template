"""GraphQL Types."""
import re
from typing import List, Optional, Sequence

from graphql.language import FieldNode
from graphql.type import GraphQLResolveInfo

from src.types.errors import GraphQLUtilsErrorMessages

ACRONYMS = ["QL", "HTTPS", "HTTP", "API"]


class GraphQLUtils:
    """Utilities for GraphQL."""

    resolve_info: GraphQLResolveInfo

    def __init__(
        self,
        *,
        info: Optional[GraphQLResolveInfo] = None,
        acronyms: Optional[List[str]] = None,
    ):
        """Initialize GraphQLUtils.

        Args:
            info (Optional[GraphQLResolveInfo]): GraphQLResolveInfo; defaults to None
            acronyms (Optional[List[str]]): list of acronyms to refer to when converting casing; defaults to a predefined list of acronyms
        """
        self.info = info
        # explicitly check for None, since [] is falsey
        self.acronyms = ACRONYMS if acronyms is None else acronyms

    def camel_case_to_snake_case(
        self, value: str, *, keep_acronyms: bool = False
    ) -> str:
        """Convert camelCase to snake_case.

        Args:
            value (str): value to convert
            keep_acronyms (bool): prevents acronyms from being split with underscores; defaults to False

        Returns:
            str: the converted value
        """
        if keep_acronyms:
            for acronym in self.acronyms:
                if acronym.upper() in value or acronym.lower() in value:
                    replacement = acronym[0].upper() + acronym[1:].lower()
                    value = value.replace(acronym, replacement)
        return re.sub(r"(?<!^)(?=[A-Z])", "_", value).lower()

    def get_projection(
        self, path: str | List[str], *, separator: str = "."
    ) -> List[str]:
        """Get projection from GraphQLResolverInfo.

        Args:
            path (str | List[str]): path to the field to get projection from
            separator (str): separator to split on when path is a string, defaults to .

        Raises:
            ValueError: when info is None or path is not found

        Returns:
            List[str]: list of projected fields
        """
        if self.info is None:
            raise ValueError(GraphQLUtilsErrorMessages.CANNOT_GET_PROJECTION)
        if isinstance(path, str):
            path = path.split(separator)
        nodes: Sequence[FieldNode] = self.info.field_nodes
        for index, field in enumerate(path):
            found = False
            for field_node in nodes:
                if (
                    field_node.name.value == field
                    and field_node.selection_set is not None
                ):
                    found = True
                    nodes = list(*field_node.selection_set.selections)
                    break
            if not found:
                raise ValueError(
                    GraphQLUtilsErrorMessages.projection_not_found(
                        path[: index + 1], path
                    )
                )
        return [
            self.camel_case_to_snake_case(selection.name.value) for selection in nodes
        ]
