from playwright.sync_api import sync_playwright
from core.db.db import DBManager
from config.config import load_config
from page_objects.page.auth import AuthPage
from page_objects.page.help import HelpPage
from page_objects.page.mill_tests import MMILPage
from page_objects.page.user import UsersPage

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
    page.goto(conf.urls.base)
    modal = page.locator('//div[@data-locator="WrapModal"]')
    if modal.is_visible():
        page.locator('//button[//text()="Обновить"]').click()
    page = AuthPage(page)
    yield page


@pytest.fixture()
def help_page(main_page, conf, request):
    page = main_page
    page.goto(conf.urls.help)
    modal = page.locator('//div[@data-locator="WrapModal"]')
    if modal.is_visible():
        page.locator('//button[//text()="Обновить"]').click()
    page = HelpPage(page)
    yield page


@pytest.fixture()
def users_page(main_page, conf, request):
    page = main_page
    page.goto(conf.urls.users)
    modal = page.locator('//div[@data-locator="WrapModal"]')
    if modal.is_visible():
        page.locator('//button[//text()="Обновить"]').click()
    page = UsersPage(page)
    yield page


@pytest.fixture()
def page_t(main_page, conf, request):
    page = main_page
    page.goto(conf.urls.mmil)
    page = MMILPage(page)
    yield page


@pytest.fixture
def test_user(db):
    user = db.create_user('patient')
    yield user
    db.delete_user(user["id"])
