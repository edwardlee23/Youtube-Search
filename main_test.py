import pytest
from httpx import AsyncClient

from main import app


@pytest.mark.anyio
async def test_get_index():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "Enter a keyword, and the three most relevant videos will be displayed." in response.text
