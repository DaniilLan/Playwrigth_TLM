import time

import pytest
from playwright.sync_api import Page, Playwright, sync_playwright
from PageLocators.locators import *
from tests.config import *


@pytest.fixture()
def main_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        context = browser.new_context(storage_state="state.json")
        page = context.new_page()
        yield page

#
# @pytest.fixture()
# def page_general(main_page):
#     page = Locators(main_page)
#     yield page
#
#
# @pytest.fixture()
# def page_auth(main_page):
#     page = main_page
#     page.goto(url_auth_test)
#     page = Locators(main_page)
#     yield page
#


@pytest.fixture()
def page_users(main_page):
    page = main_page
    page.goto(url_users_test)
    page = Locators(main_page)
    yield page


# @pytest.fixture()
# def page_help(main_page):
#     page = main_page
#     page.goto(url_help_test)
#     page = Locators(main_page)
#     yield page
#
#
# @pytest.fixture()
# def page_support(main_page):
#     page = main_page
#     page.goto(url_support_test)
#     page = Locators(main_page)
#     yield page
#
#
#
