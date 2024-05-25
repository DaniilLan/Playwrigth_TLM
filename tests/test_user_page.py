from tests.config import *
import time
import pytest
import json


@pytest.mark.parametrize('mail, name', [(mail, name) for mail, name in cred.items()])
@pytest.mark.parametrize('password', [password_all])
def test_auth_and_save_cookies(page_auth, mail, password, name):
    page_auth.test_login_users(page_auth, mail, password)
    user = page_auth.get_text(page_auth.NAME_USER)
    assert user == name, f"Имя пользователя не соответствует кредам"
    page_auth.wait_visible_all()
    page_auth.screenshot(dop=mail)
    # update project
