from fastapi import FastAPI,Form

app = FastAPI()


database = [
    {"concat":"this is concat"},
    {"add":"this is add"}
]

@app.get("/{query}")
async def graphql(
    query:str
):
    if query:
        try:
            for item in database:
                if query in item:
                    return item[query]
        except Exception as e:
            return str(e)
    
    return query