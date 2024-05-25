import pytest
from playwright.sync_api import Page
from PageLocators.locators import LocatorsPage
from tests.config import *


@pytest.fixture()
def main_page(context):
    page: Page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page


@pytest.fixture()
def page_auth(main_page):
    page = LocatorsPage(main_page)
    page.open(url_auth_test)
    yield page


