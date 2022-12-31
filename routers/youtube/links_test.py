import pytest
from httpx import AsyncClient

from main import app


@pytest.mark.anyio
async def test_get_youtube_links_without_keyword():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/youtube/links?keyword=")
    assert response.status_code == 200
    assert response.text == "Please enter a keyword. The field cannot be left blank."


@pytest.mark.anyio
async def test_get_youtube_links_with_keyword_hello():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/youtube/links?keyword=hello")
    assert response.status_code == 200
    assert "https://www.youtube.com/watch?v=YQHsXMglC9A" in response.text
