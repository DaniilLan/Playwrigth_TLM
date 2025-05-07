from playwright.sync_api import sync_playwright
from core.db.db import DBManager
from config.config import load_config

import pytest

from page_objects.page.auth import AuthPage


@pytest.fixture(scope="class")
def db():
    return DBManager()


@pytest.fixture()
def conf():
    return load_config()


@pytest.fixture()
def settings_page(conf):
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
def auth_page(settings_page, conf, request):
    page = settings_page
    page.goto(conf.urls.base)
    page = AuthPage
    yield page


@pytest.fixture
def test_user(db):
    user = db.create_user()
    yield user
    db.delete_user(user["id"])


@pytest.fixture
def doctor_emails(conf):
    return conf.doctor_emails


@pytest.fixture
def admin_emails(conf):
    return conf.admin_emails

