from functools import wraps
from typing import Union, List, Optional
from playwright.sync_api import expect, Page, Locator
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from locators.auth_locators import LocatorsAuth
from locators.user_locators import LocatorsUsers

import logging
import inspect



def handle_playwright_errors(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except PlaywrightTimeoutError as e:
            method_name = func.__name__
            locator = args[0] if args else "unknown"
            error_msg = f"Timeout in {method_name}(locator='{locator}'): {e}"
            logging.error(error_msg)
            self._take_screenshot(method_name, "timeout_error")
            raise PlaywrightTimeoutError(error_msg) from e
        except Exception as e:
            method_name = func.__name__
            error_msg = f"Error in {method_name}: {e}"
            logging.error(error_msg)
            self._take_screenshot(method_name, "error")
            raise
    return wrapper


class MethodsPage:
    def __init__(self, page: Page):
        self.page = page
        self.CLICK_DELAY_MS = 500

    def _take_screenshot(self, method_name: str, error_type: str):
        """Внутренний метод для создания скриншотов при ошибках"""
        screenshot_path = (
            f"screenshot_tests/{method_name}/{method_name}_{error_type}.png"
        )
        self.page.screenshot(path=screenshot_path, full_page=True)

    @handle_playwright_errors
    def open(self, uri: str):
        """Открыть страницу"""
        self.page.goto(uri)

    @handle_playwright_errors
    def get_uri(self):
        """Получить URI"""
        return self.page.url

    @handle_playwright_errors
    def click(self, locator: str):
        """Кликнуть по элементу"""
        self.page.click(locator)

    @handle_playwright_errors
    def click_on_elements(self, locator: str):
        """Кликнуть по всем элементам, соответствующим локатору"""
        elements = self.page.locator(locator).all()
        for element in elements:
            self.page.wait_for_timeout(self.CLICK_DELAY_MS)
            element.click()

    @handle_playwright_errors
    def fill_text(self, locator: str, value: str):
        """Ввод текста в поле"""
        element = self.page.locator(locator)
        expect(element).to_be_visible()
        element.fill(value)

    @handle_playwright_errors
    def get_text(self, locator: str):
        """Получить текст элемента"""
        return self.page.locator(locator).text_content()

    @handle_playwright_errors
    def expect_text(self, locator: str, text_element: str):
        """Проверка соответствия текста ОР"""
        locator = self.page.locator(locator)
        expect(locator).to_have_text(text_element)

    @handle_playwright_errors
    def get_list_text(self, locator: str):
        """Получить объединенный текст всех элементов"""
        elements = self.page.locator(locator).all()
        return "".join(element.text_content() for element in elements)

    @handle_playwright_errors
    def wait_visible_elements(self, locators: Union[str, List[str]], timeout_sec: int = 30):
        """Ожидать появления элемента(ов)"""
        locators_list = [locators] if isinstance(locators, str) else locators
        for locator in locators_list:
            self.page.wait_for_selector(
                locator,
                state="visible",
                timeout=timeout_sec * 1000
            )

    @handle_playwright_errors
    def login_users(self, mail: str, password: str):
        """Авторизация пользователя"""
        self.fill_text(LocatorsAuth.INPUT_MAIL, mail)
        self.fill_text(LocatorsAuth.INPUT_PASSWORD, password)
        self.click(LocatorsAuth.BUTTON_LOG)
        self.wait_visible_elements(LocatorsUsers.NAME_PROFILE)

    @handle_playwright_errors
    def expect_not_visible_elements(self, locators: Union[str, List[str]]):
        """Проверка - элемент не виден"""
        locators_list = [locators] if isinstance(locators, str) else locators
        for locator in locators_list:
            expect(self.page.locator(locator)).not_to_be_visible()

    @handle_playwright_errors
    def expect_visible_elements(self, locators: Union[str, List[str]]):
        """Проверка - элемент виден"""
        locators_list = [locators] if isinstance(locators, str) else locators
        for locator in locators_list:
            expect(self.page.locator(locator)).to_be_visible()

    @handle_playwright_errors
    def dropdown_filter(self):
        """Опустить drop-down список 'Фильтры' - изменив параметр элемента в DOM"""
        element = self.page.locator('//*[@id="rootTelemedHub"]/div[2]/main/div/div[2]/div/div')
        element.evaluate('(element) => { element.style.maxHeight = "none"; }')

    @handle_playwright_errors
    def open_dropdown_organization(self):
        """Раскрыть все видимые организации в поле 'Организации' при добавлении пользователя"""
        self.page.click(LocatorsUsers.FILTER_DROPDOWN_ORG)
        elements = self.page.locator('//div[@class="arrowControl__e920 arrowControl"]').all()
        col = 0
        while col != len(elements):
            self.click('//div[@class="arrowControl__e920 arrowControl"]')
            col += 1

    @handle_playwright_errors
    def get_quantity_elements(self, locator: str):
        """Получить количество элементов"""
        elements = self.page.locator(locator).all()
        return len(elements)

    @handle_playwright_errors
    def get_attribute_element(self, locator, type_attribute: str):
        """Получить атрибуты элемента"""
        element = self.page.locator(locator)
        return element.get_attribute(type_attribute)

    @handle_playwright_errors
    def expect_style_element(self, locator, name_style: str, value_style: str):
        """Проверка - 'имя' и 'значение' стиля элемента равны заданным параметрам (name_style, value_style)"""
        element = self.page.locator(locator)
        return expect(element).to_have_css(name_style, value_style)

    @handle_playwright_errors
    def change_password(self, current_pass: str, new_pass: str):
        """Смена пароля на стр. /users в профиле пользователя"""
        self.page.fill(LocatorsUsers.INPUT_CURRENT_PASS, current_pass)
        self.page.fill(LocatorsUsers.INPUT_NEW_PASS, new_pass)
        self.page.fill(LocatorsUsers.INPUT_NEW2_PASS, new_pass)

    @handle_playwright_errors
    def expect_invalid_input_color(self, locator_placeholder: Union[str, List[str]],
                                         locator_body_input: Union[str, List[str]]):
        """Проверка - что цвет плейсхолдера и тела поля(лей)
        при вводе не валидных данных соответствует цвету при ошибке"""
        if type(locator_placeholder) is not list:
            self.expect_style_element(locator_placeholder, 'color', 'rgb(229, 74, 76)')
        else:
            for locator in locator_placeholder:
                self.expect_style_element(locator, 'color', 'rgb(229, 74, 76)')
        if type(locator_body_input) is not list:
            self.expect_style_element(locator_body_input, 'background-color', 'rgb(255, 243, 242)')
            self.expect_style_element(locator_body_input, 'border-color', 'rgb(229, 74, 76)')
        else:
            for locator in locator_body_input:
                self.expect_style_element(locator, 'background-color', 'rgb(255, 243, 242)')
                self.expect_style_element(locator, 'border-color', 'rgb(229, 74, 76)')

    @handle_playwright_errors
    def clear_inputs(self, locators: Union[str, List[str]]):
        """Очистить поле ввода"""
        locators_list = [locators] if isinstance(locators, str) else locators
        for locator in locators_list:
            self.page.locator(locator).clear()
