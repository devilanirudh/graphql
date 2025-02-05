from fastapi import FastAPI
from strawberry.asgi import GraphQL
import strawberry

course_name="computer science"
course_time_year=1
app = FastAPI()

@strawberry.type
class course:
    @strawberry.field
    def name(self) ->str:
        return course_name
    @strawberry.field
    def duration(self) -> str:
        return course_time_year
    
schema=strawberry.Schema(query=course)
graphql_app = GraphQL(schema)
print(schema)
app.add_route("/graphql",graphql_app)

