from playwright.sync_api import expect
from playwright.sync_api import Page
import inspect
import json
import pytest
from tests.config import *


class MethodsPageUsers:

    def __init__(self, page: Page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def get_url(self):
        return self.page.url

    def click(self, locator):
        self.page.click(locator)

    def fill_text(self, locator, value):
        element = self.page.locator(locator)
        expect(element).to_be_visible()
        self.page.fill(locator, value)

    def get_text(self, locator):
        return self.page.text_content(locator)

    def wait_visible_element(self, locator):
        element = self.page.locator(locator)
        expect(element).to_be_visible()

    def wait_visible_all(self):
        all_elements = self.page.query_selector_all("*")
        for element in all_elements:
            element.is_visible()

    def screenshot_full(self, dop=None):
        current_function_name = inspect.stack()[1].function
        self.page.screenshot(path=f"screenshot_tests/{current_function_name}_{dop}.png", full_page=True)

    def screenshot(self, dop=None):
        current_function_name = inspect.stack()[1].function
        self.page.screenshot(path=f"screenshot_tests/{current_function_name}_{dop}.png")

    def test_login_users(self, page_auth, mail, password):
        page_auth.fill_text(page_auth.INPUT_MAIL, mail)
        page_auth.fill_text(page_auth.INPUT_PASSWORD, password)
        page_auth.click(page_auth.BUTTON_LOG)
