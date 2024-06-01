import pytest
from playwright.sync_api import Page
from PageLocators.locators import *
from tests.config import *


@pytest.fixture()
def main_page(context):
    page: Page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page


@pytest.fixture()
def general_page(main_page):
    page = Locators(main_page)
    yield page


@pytest.fixture()
def page_auth(main_page):
    page = main_page
    page.goto(url_auth_test)
    page = Locators(main_page)
    yield page


@pytest.fixture()
def page_users(main_page):
    page = main_page
    page.goto(url_users_test)
    page = Locators(main_page)
    yield page


@pytest.fixture()
def page_help(main_page):
    page = main_page
    page.goto(url_help_test)
    page = Locators(main_page)
    yield page


@pytest.fixture()
def page_support(main_page):
    page = main_page
    page.goto(url_support_test)
    page = Locators(main_page)
    yield page



