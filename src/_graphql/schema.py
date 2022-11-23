from ariadne import make_executable_schema, snake_case_fallback_resolvers

from . import query, type_defs
from .queries import *

schema = make_executable_schema(type_defs, query, snake_case_fallback_resolvers)
