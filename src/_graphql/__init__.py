from ariadne import ObjectType, gql, load_schema_from_path

SCHEMA_PATH = "src/_graphql/schemas"

type_defs = gql(load_schema_from_path(SCHEMA_PATH))

query = ObjectType("Query")
