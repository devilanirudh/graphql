from fastapi import FastAPI
from strawberry.asgi import GraphQL
import strawberry
from typing import List

data = [
    {
        "name":"Roni",
        "city":"cologne"
    },
    {
        "name":"johm",
        "city":"London"
    },
    {
        "name":"Maria",
        "city":"sydney"
    }
]

# def resolve_student(self):
#     return data

@strawberry.type
class student:
    @strawberry.field
    name=str
    city=str

def resolve_students() -> List[student]:
    return [student(**student) for student in data]

@strawberry.type
class Query:
    students: List[student] = strawberry.field(resolver=resolve_students)

# Schema
schema = strawberry.Schema(query=Query)

app = FastAPI()

graphql_app = strawberry.Schema(query=Query)
app.add_route("/qlperson",graphql_app)