import pytest
import requests


def get_token():
    auth_url = "http://192.168.7.35:5003/api/auth/sign-in"
    auth_data = {
        "email": "testdoctor@mail.ru",
        "password": "Testdoctor1!"
    }

    try:
        response = requests.post(auth_url, json=auth_data)
        response.raise_for_status()
        token = response.json().get("token")
        if not token:
            raise ValueError("Токен не найден в ответе API")
        else:
            return token
    except Exception as e:
        pytest.fail(f"Ошибка при получении токена: {str(e)}")

