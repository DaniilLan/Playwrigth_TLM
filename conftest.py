from playwright.sync_api import sync_playwright
from page_objects.base_page import BasePage
from core.db.db import DBManager
from config.config import load_config

import pytest


@pytest.fixture(scope="session")
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
def page(main_page, conf, request):
    page = main_page
    url = conf.urls.base
    page.goto(url)
    request.cls.conf = conf
    request.cls.page = BasePage(page, conf)
    yield



@pytest.fixture
def test_user(db):
    user = db.create_user()
    yield user
    db.delete_user(user["id"])