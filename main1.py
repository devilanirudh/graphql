from fastapi import FastAPI
from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL
import graphene

type_defs = """
    type Query {
        concat: String!
        add: String!
    }
"""

query = QueryType()

@query.field("concat")
def resolve_concat(_, info,a:str,b:str):
    return a+b

@query.field("add")
def resolve_add(_, info):
    return "This is adding"

schema = make_executable_schema(type_defs, query)

app = FastAPI()

# Use Ariadne’s GraphQL server
app.add_route("/graphql", GraphQL(schema))

# Run using: uvicorn main:app --reload
