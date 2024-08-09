import time
import pytest
from playwright.sync_api import Page, Playwright, sync_playwright
from PageLocators.locators import *
from tests.config import *


@pytest.fixture()
def main_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=300)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()
        page = Locators(page)
        yield page


@pytest.fixture()
def page_auth(main_page):
    page = main_page
    page.open(url_auth_test)
    yield page


@pytest.fixture()
def page_users(main_page):
    page = main_page
    page.open(url_users_test)
    yield page


@pytest.fixture()
def page_help(main_page):
    page = main_page
    page.open(url_help_test)
    yield page


@pytest.fixture()
def page_support(main_page):
    page = main_page
    page.open(url_support_test)
    yield page
