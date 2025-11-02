from fastapi import FastAPI, Request

from app_lifespan import lifespan
from api import router as api_router


app = FastAPI(
    title="Example-Base-App",
    lifespan=lifespan,
)


@app.get("/")
def read_root(request: Request) -> dict[str, str]:
    docs_url = request.url.replace(
        path="/docs",
        query="",
    )
    return {
        "docs": str(docs_url),
    }


app.include_router(api_router)
