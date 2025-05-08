from playwright.sync_api import sync_playwright
from core.db.db import DBManager
from config.config import load_config
from page_objects.page.auth import AuthPage

import pytest


@pytest.fixture(scope="class")
def db():
    return DBManager()


@pytest.fixture()
def conf():
    return load_config()


@pytest.fixture()
def main_page(conf):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=300,
        )
        context = browser.new_context(
            viewport=conf.context.viewport_fhd,
        )
        page = context.new_page()
        yield page


@pytest.fixture()
def auth_page(main_page, conf, request):
    page = main_page
    page = AuthPage(page)
    yield page


@pytest.fixture
def test_user(db):
    user = db.create_user()
    yield user
    db.delete_user(user["id"])
