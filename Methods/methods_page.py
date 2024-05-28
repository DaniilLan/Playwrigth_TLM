import re
from playwright.sync_api import expect
from playwright.sync_api import Page
import inspect
import json
import pytest
from tests.config import *
from playwright.sync_api import Route


class MethodsPageUsers:

    def __init__(self, page: Page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def get_url(self):
        return self.page.url

    def click(self, locator):
        self.page.click(locator, timeout=5000)

    def click_on_elements(self, locator):
        elements = self.page.locator(locator).all()
        for element in elements:
            element.click(timeout=5000)

    def fill_text(self, locator, value):
        element = self.page.locator(locator)
        expect(element).to_be_visible()
        self.page.fill(locator, value)

    def get_text(self, locator):
        return self.page.text_content(locator, strict=False)

    def wait_load_page(self):
        self.page.wait_for_load_state()

    def wait_visible_all(self):
        all_elements = self.page.query_selector_all("*")
        for element in all_elements:
            element.is_visible()

    def expect_visible_element(self, locator):
        expect(self.page.locator(locator)).to_be_visible()

    def expect_visible_text(self, locator):
        text = self.get_text(locator)
        expect(self.page.get_by_text(text)).to_be_visible()

    def screenshot_full(self, dop=None):
        current_function_name = inspect.stack()[1].function
        self.page.screenshot(path=f"screenshot_tests/{current_function_name}/{current_function_name}_{dop}.png",
                             full_page=True)

    def screenshot(self, dop=None):
        current_function_name = inspect.stack()[1].function
        self.page.screenshot(path=f"screenshot_tests/{current_function_name}/{current_function_name}_{dop}.png")

    def login_users(self, page_auth, mail, password):
        page_auth.fill_text(page_auth.INPUT_MAIL, mail)
        page_auth.fill_text(page_auth.INPUT_PASSWORD, password)
        page_auth.click(page_auth.BUTTON_LOG)

    def expect_visible_elements(self, locator):
        elements = self.page.locator(locator).all()
        for element in elements:
            return expect(element).to_be_visible()

    def dropdown_filter(self):
        element = self.page.locator('//*[@id="rootTelemedHub"]/div[2]/main/div/div[2]/div[1]/div/div')
        element.evaluate('(element) => { element.style.maxHeight = "none"; }')

    def get_quantity_elements(self, locator):
        elements = self.page.locator(locator).all()
        return len(elements)
