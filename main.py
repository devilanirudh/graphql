#working strawberry
from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL

# Define a proper Strawberry type
@strawberry.type
class Calculator:
    @strawberry.field
    def concat(self,a:str,b:str) -> str:
        return a+b

    @strawberry.field
    def add(self,a:int,b:int) -> str:
        return a+b

# Define the schema correctly
schema = strawberry.Schema(query=Calculator)

# Create the FastAPI app
app = FastAPI()

# Mount GraphQL app properly
graphql_app = GraphQL(schema)
app.add_route("/graphql", graphql_app)

