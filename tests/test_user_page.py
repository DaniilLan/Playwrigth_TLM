from tests.config import *
import time
import pytest
import json
from playwright.sync_api import Route


@pytest.mark.parametrize('mail, name', [(mail, name) for mail, name in cred.items()])
@pytest.mark.parametrize('password', [password_all])
def test_auth(page_auth, mail, password, name):
    page_auth.login_users(page_auth, mail, password)
    page_auth.wait_load_page()
    page_auth.screenshot(dop=mail)
