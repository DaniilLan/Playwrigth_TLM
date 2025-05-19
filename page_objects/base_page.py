from functools import wraps
from inspect import signature
from typing import Callable, Any, Union, List
from playwright.sync_api import expect, Page
from config.config import load_config
from playwright.sync_api import (
    TimeoutError as PlaywrightTimeoutError,
    Error as PlaywrightError
)

import logging
import urllib.parse
import re


def handle_playwright_errors(func: Callable) -> Callable:
    """Декоратор для обработки ошибок Playwright"""

    @wraps(func)
    def wrapper(self, *args, **kwargs) -> Any:
        method_name = func.__name__
        sig = signature(func)
        bound_args = sig.bind(self, *args, **kwargs)

        locator_param = next((param for param in sig.parameters.values()
                              if param.name.lower() == 'locator'), None)
        locator = bound_args.arguments.get(locator_param.name, "unknown") if locator_param else "unknown"
        try:
            return func(self, *args, **kwargs)
        except PlaywrightTimeoutError as e:
            error_msg = f"TimeoutError in {method_name}(locator='{locator}'): {str(e)}"
            logging.error(error_msg)
            self._take_screenshot(method_name, "playwright_timeout")
            raise PlaywrightTimeoutError(error_msg) from e
        except PlaywrightError as e:
            error_type = type(e).__name__
            error_msg = f"{error_type} in {method_name}(locator='{locator}'): {str(e)}"
            logging.error(error_msg)
            self._take_screenshot(method_name, f"playwright_{error_type.lower()}")
            raise type(e)(error_msg) from e
        except AssertionError as e:
            logging.error(f"Validation failed in {method_name}(locator='{locator}'): {str(e)}")
            self._take_screenshot(method_name, "validation_error")
            raise
        except Exception as e:
            logging.error(f"UNEXPECTED error in {method_name}: {type(e).__name__} - {str(e)}", exc_info=True)
            raise

    return wrapper


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.conf = load_config()

    def _take_screenshot(self, method_name: str, error_type: str):
        """Внутренний метод для создания скриншотов при ошибках"""
        screenshot_path = (
            f"screenshot_tests/{method_name}/{method_name}_{error_type}.png"
        )
        self.page.screenshot(path=screenshot_path, full_page=True)

    @handle_playwright_errors
    def log_in(self, mail, locator_mail, locator_password, locator_button):
        """Авторизация"""
        self.fill_text(locator_mail, mail)
        self.fill_text(locator_password, self.conf.creds.password_valid)
        self.click(locator_button)

    @handle_playwright_errors
    def open(self, uri: str):
        """Открыть страницу"""
        self.page.goto(uri)
        self.page.wait_for_load_state()

    @handle_playwright_errors
    def get_url(self):
        """Получить URI"""
        return self.page.url

    @handle_playwright_errors
    def click(self, locator: str):
        """Кликнуть по элементу"""
        self.wait_visible_elements(locator)
        self.page.click(locator)

    @handle_playwright_errors
    def click_on_elements(self, locator: str):
        """Кликнуть по всем элементам, соответствующим локатору"""
        elements = self.page.locator(locator).all()
        for element in elements:
            expect(element).to_be_visible()
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
        element = self.page.locator(locator)
        return expect(element).to_have_text(text_element)

    @handle_playwright_errors
    def get_list_text(self, locator: str):
        """Получить объединенный текст всех элементов"""
        elements = self.page.locator(locator).all()
        text = "".join(element.text_content() for element in elements)
        if text is None:
            raise ValueError(f"У элемента с локатором = {locator}, отсутствует текст")
        return text

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
    def expect_not_visible_elements(self, locators: Union[str, List[str]]):
        """Проверка - элемент не виден"""
        locators_list = [locators] if isinstance(locators, str) else locators
        for locator in locators_list:
            return expect(self.page.locator(locator)).not_to_be_visible()

    @handle_playwright_errors
    def expect_visible_elements(self, locators: Union[str, List[str]]):
        """Проверка - элементы видны"""
        locators_list = [locators] if isinstance(locators, str) else locators
        for locator in locators_list:
            if self.page.is_visible(locator):
                return True
        return False

    @handle_playwright_errors
    def get_quantity_elements(self, locator: str):
        """Получить количество элементов"""
        elements = self.page.locator(locator).all()
        return len(elements)

    @handle_playwright_errors
    def get_attribute_element(self, locator: str, type_attribute: str):
        """Получить атрибуты элемента"""
        element = self.page.locator(locator)
        return element.get_attribute(type_attribute)

    @handle_playwright_errors
    def expect_style_element(self, locator, name_style: str, value_style: str):
        """Проверка - 'имя' и 'значение' стиля элемента равны заданным параметрам (name_style, value_style)"""
        element = self.page.locator(locator)
        return expect(element).to_have_css(name_style, value_style)


    @handle_playwright_errors
    def expect_style_element(self, locator: str, name_style: str, value_style: str):
        """Проверка - 'имя' и 'значение' стиля элемента равны заданным параметрам"""
        element = self.page.locator(locator) if not locator.startswith('/') else self.page.locator(f'xpath={locator}')
        return expect(element).to_have_css(name_style, value_style)

    @handle_playwright_errors
    def expect_invalid_input_color(self, locator_placeholder: Union[str, List[str]],
                                   locator_body_input: Union[str, List[str]]):
        """Проверка цвета при ошибке валидации"""
        if not isinstance(locator_placeholder, list):
            self.expect_style_element(locator_placeholder, 'color', self.conf.css.error_border_color)
        else:
            for locator in locator_placeholder:
                self.expect_style_element(locator, 'color', self.conf.css.error_border_color)

        if not isinstance(locator_body_input, list):
            self.expect_style_element(locator_body_input, 'background-color', self.conf.css.error_background_color)
            self.expect_style_element(locator_body_input, 'border-color', self.conf.css.error_border_color)
        else:
            for locator in locator_body_input:
                self.expect_style_element(locator, 'background-color', self.conf.css.error_background_color)
                self.expect_style_element(locator, 'border-color', self.conf.css.error_border_color)

    @handle_playwright_errors
    def clear_inputs(self, locators: Union[str, List[str]]):
        """Очистить поле ввода"""
        locators_list = [locators] if isinstance(locators, str) else locators
        for locator in locators_list:
            self.page.locator(locator).clear()
            return expect(self.page.locator(locator)).to_be_empty()

    @handle_playwright_errors
    def expect_css_style(self, locator: str, name_css: str, param_css: str):
        """Проверка параметров стиля элемента"""
        element = self.page.locator(locator)
        return expect(element).to_have_css(name_css, param_css)

    @handle_playwright_errors
    def hovering_on_element(self, locator: str):
        """Навестить курком на элемент."""
        self.wait_visible_elements(locator)
        self.page.hover(locator)

    @handle_playwright_errors
    def expect_url(self, url: str):
        """Ожидание конкретного URL на текущей странице"""
        self.page.wait_for_url(url)
        self.page.wait_for_load_state()

    @handle_playwright_errors
    def expect_url_pdf(self, url_pdf: str, locator: str):
        """Ожидание открытого URL (PDF)"""
        with self.page.context.expect_page() as new_page_info:
            self.click(locator)
        new_page = new_page_info.value
        decoded_url = urllib.parse.unquote(new_page.url)
        assert decoded_url == url_pdf, (f"Страница файла не соответствует ожиданию"
                                        f"Текущая: {decoded_url}"
                                        f"Ожидаемая: {url_pdf}")

    @handle_playwright_errors
    def element_has_class(self, locator: str, expected_class: str):
        """Ожидание определенного класса у элемента - True/False"""
        self.page.wait_for_selector(locator, state="visible")
        class_attribute = self.page.get_attribute(locator, "class")
        return class_attribute is not None and expected_class in class_attribute.split()

    @handle_playwright_errors
    def expect_open_element(self, locator):
        """Проверка, что элемент открыт и имеет класс open__db7c"""
        self.wait_visible_elements(locator)
        expect_item = self.element_has_class(locator, 'open__db7c')
        assert expect_item, f"Элемент не виден, либо отсутствует нужный класс элемента 'open__db7c'"