from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from models.youtube_search import YoutubeSearch

router = APIRouter(
    prefix="/youtube",
    tags=["youtube"],
    responses={404: {"description": "Not found"}},
)


@router.get("/links", response_class=HTMLResponse)
async def get_youtube_links(keyword: str):
    if not keyword:
        return "Please enter a keyword. The field cannot be left blank."
    return await YoutubeSearch(keyword).get_youtube_links()
