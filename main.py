from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from routers.youtube import links

description = """
Enter a keyword, and the three most relevant videos will be displayed.

## Index

You can **search youtube videos**.

## Youtube

You can **get youtube videos**.
"""

tags_metadata = [
    {
        "name": "index",
        "description": "Get the index webpage.",
    },
    {
        "name": "youtube",
        "description": "Get the three most relevant videos.",
    },
]

app = FastAPI(
    title="Youtube Search",
    description=description,
    version="0.0.1",
    docs_url="/documentation",
    redoc_url=None,
    openapi_tags=tags_metadata,
)

app.include_router(links.router)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse, tags=['index'])
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
