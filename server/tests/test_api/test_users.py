import pytest
from httpx import AsyncClient
from package.auth import decode_access_token
from starlette import status

from api.responses import AuthDetail
from config import get_app_settings
from conftest import get_auth_url


class TestUser:

    @pytest.mark.asyncio
    async def test_get_all_users(
            self,
            client: AsyncClient,
            superuser_headers: dict,
    ):
        resp = await client.get(get_auth_url("get_all_users"), headers=superuser_headers)
        assert resp.status_code == status.HTTP_200_OK
        print(resp.json())
        # assert len(resp.json()) == 1
        assert resp.json()[0]['username'] == 'admin'

    async def test_create_user(
            self,
            client: AsyncClient,
    ):
        pass

    @pytest.mark.asyncio
    async def test_token_login_superuser(
            self,
            client: AsyncClient,
    ):
        settings = get_app_settings()
        data = {
            "username": settings.SUPERUSER_NAME,
            "password": settings.SUPERUSER_PASSWORD
        }
        resp = await client.post(url=get_auth_url("get_token"), json=data)
        token = resp.json()['access_token']
        decoded_token = decode_access_token(token)
        assert decoded_token['username'] == data['username']

    @pytest.mark.asyncio
    async def test_token_login(
            self,
            client: AsyncClient,
            user_data: dict
    ):
        await client.post(url=get_auth_url("register_user"), json=user_data)
        login_data = {
            "username": user_data['username'],
            "password": user_data['password']
        }
        resp = await client.post(url=get_auth_url("get_token"), json=login_data)
        token = resp.json()['access_token']
        decoded_token = decode_access_token(token)
        assert decoded_token['username'] == user_data['username']

    @pytest.mark.asyncio
    async def test_register_user(
            self,
            client: AsyncClient,
            user_data: dict
    ):
        resp = await client.post(url=get_auth_url("register_user"), json=user_data)
        assert resp.status_code == status.HTTP_200_OK
        user_show_data = resp.json()
        assert user_show_data['username'] == user_data['username']

    @pytest.mark.asyncio
    async def test_token_fail(
            self,
            client: AsyncClient,
            user_data: dict
    ):
        login_data = {
            "username": user_data['username'],
            "password": user_data['password']
        }
        resp = await client.post(url=get_auth_url("get_token"), json=login_data)
        assert resp.status_code == status.HTTP_403_FORBIDDEN
        assert resp.json() == {"detail": AuthDetail.login_data_error.value}

    @pytest.mark.asyncio
    async def test_get_all_users_fail(
            self,
            client: AsyncClient,
            common_headers: dict
    ):
        resp = await client.get(url=get_auth_url("get_all_users"), headers=common_headers)
        assert resp.status_code == status.HTTP_403_FORBIDDEN
        assert resp.json() == {"detail": AuthDetail.no_permissions.value}

    # @pytest.mark.asyncio
    # async def test_environ(self):
    #     print(os.environ)
    #     assert "TEST" in os.environ
