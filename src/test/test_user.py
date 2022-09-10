from faker import Faker
import pytest
from httpx import AsyncClient
from src.router.main import app

user={
    "nome":Faker.name(),
    "email":Faker.email(),
    'senha':Faker.password()
}


@pytest.mark.asyncio
async def test_crete_user():
    async with AsyncClient(app=app,base_url='http://test')as ac:
        response= await ac.post("/user/",data=user)
    assert response.status_code == 201
