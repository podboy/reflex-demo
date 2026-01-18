from fastapi import Query

from .fastapi import fastapi_app


# Add routes to the FastAPI app
@fastapi_app.get("/api/hello")
async def hello(name: str = Query(default="world", min_length=3)):
    return f"hello {name}"
