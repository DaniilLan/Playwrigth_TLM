from playwright.sync_api import sync_playwright
from core.db.db import DBManager
from config.config import load_config

import pytest

from page_objects.page.auth import AuthPage


@pytest.fixture(scope="class")
def db():
    return DBManager()


@pytest.fixture(autouse=True)
def conf():
    return load_config()


@pytest.fixture()
def settings_browser(conf):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=300,
        )
        context = browser.new_context(
            viewport=conf.context.viewport_fhd,
        )
        browser = context.new_page()
        yield browser


@pytest.fixture()
def page_auth(settings_browser, conf, request):
    page = settings_browser
    page.goto(conf.urls.base)
    page = AuthPage(page)
    yield page


@pytest.fixture
def test_user(db):
    user = db.create_user()
    yield user
    db.delete_user(user["id"])
