from playwright.sync_api import sync_playwright
from page.base_page import *
from core.db.db import DBManager
from config.config import load_config

import pytest


@pytest.fixture()
def main_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()
        yield page


@pytest.fixture(scope="session")
def db():
    return DBManager()


@pytest.fixture()
def conf():
    return load_config()


@pytest.fixture()
def page_auth(main_page, conf):
    page = main_page
    url = conf.urls.base
    page.goto(url)
    yield MethodsPageUsers(page)


@pytest.fixture
def test_user(db):
    user = db.create_user()
    yield user
    db.delete_user(user["id"])
