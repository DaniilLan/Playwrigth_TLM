import random
import time
from PageLocators.locators import LocatorsPageAuth, LocatorsPageUsers
import requests
from playwright.sync_api import expect, Page
import inspect
from typing import Union, List
from tests.config import *
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


class MethodsPageUsers:

    def __init__(self, page: Page):
        self.page = page

    def open(self, uri):
        """Открыть страницу"""
        self.page.goto(uri)

    def get_uri(self):
        """Получить URI"""
        return self.page.url

    def click(self, locator):
        """Кликнуть по элементу"""
        self.page.click(locator)

    def click_on_elements(self, locator):
        """Кликнуть по элементам"""
        elements = self.page.locator(locator).all()
        for element in elements:
            self.page.wait_for_timeout(500)
            element.click()

    def focus_inputs(self, locator):
        """Кликнуть по элементам"""
        elements = self.page.locator(locator).all()
        for element in elements:
            self.page.wait_for_timeout(500)
            element.focus()

    def fill_text(self, locator, value):
        """Ввод тескста"""
        element = self.page.locator(locator)
        expect(element).to_be_visible()
        self.page.fill(locator, value)

    def focus_element(self, locator):
        """Проверка фокуса на элементе"""
        locator = self.page.locator(locator)
        locator.focus()

    def get_text(self, locators):
        """Получить текст внутри элемента"""
        text = self.page.text_content(locators)
        return text


    def get_list_text(self, locators):
        """Получить текст внутри элементов"""
        elements = self.page.locator(locators).all()
        if type(elements) is not list:
            return self.page.text_content(locators, strict=False)
        else:
            text = ''
            for locator in elements:
                text += locator.text_content()
            print(text)
            return text


    def wait_load_page(self):
        """Ожидать полной загрузки DOM"""
        self.page.wait_for_load_state("domcontentloaded")

    def wait_visible_elements(self, locators: Union[str, List[str]], timeout: int = 30):
        if isinstance(locators, (list, tuple)):
            for locator in locators:
                try:
                    self.page.wait_for_selector(locator, state="visible", timeout=timeout * 1000)
                except PlaywrightTimeoutError as e:
                    raise PlaywrightTimeoutError(f"Элемент '{locator}' не появился за {timeout} сек.") from e #------------------------ Пример новой конструкции
        else:
            try:
                self.page.wait_for_selector(locators, state="visible", timeout=timeout * 1000)
            except PlaywrightTimeoutError as e:
                raise PlaywrightTimeoutError(f"Элемент '{locators}' не появился за {timeout} сек.") from e

    def wait_until_visible_elements(self, locators):
        """Ожидать пока элемент не пропадет"""
        if type(locators) is not list:
            try:
                self.page.wait_for_selector(locators, state='hidden')
            except PlaywrightTimeoutError:
                pass                                                                                         #-------------------------- Пример старой конструкции
        else:
            elements = self.page.locator(locators).all()
            for locator in elements:
                try:
                    locator.wait_for(state='hidden')
                except PlaywrightTimeoutError:
                    pass

    def expect_visible_text(self, locators):
        """Проверка - виден ли текст элемента"""
        text = self.get_text(locators)
        expect(self.page.get_by_text(text)).to_be_visible()

    def screenshot_full(self, dop=None):
        """Сделать скриншот всей странице (всего скролла)"""
        current_function_name = inspect.stack()[1].function
        self.page.screenshot(path=f"screenshot_tests/{current_function_name}/{current_function_name}_{dop}.png",
                             full_page=True)

    def screenshot(self, dop=None):
        """Сделать скрин стр (на позиции скролла)"""
        current_function_name = inspect.stack()[1].function
        self.page.screenshot(path=f"screenshot_tests/{current_function_name}/{current_function_name}_{dop}.png")

    def login_users(self, mail, password):
        """Авторизация пользователя"""
        self.page.fill(LocatorsPageAuth.INPUT_MAIL, mail)
        self.page.fill(LocatorsPageAuth.INPUT_PASSWORD, password)
        self.page.click(LocatorsPageAuth.BUTTON_LOG)
        self.page.wait_for_selector(LocatorsPageUsers.NAME_PROFILE)

    def expect_not_visible_elements(self, locators):
        """Проверка - элемент не виден"""
        if type(locators) is not list:
            elements = self.page.locator(locators).all()
            for element in elements:
                expect(element).not_to_be_visible()
        else:
            for locator in locators:
                expect(self.page.locator(locator)).not_to_be_visible()

    def expect_visible_elements(self, locators):
        """Проверка - элемент виден"""
        if type(locators) is not list:
            elements = self.page.locator(locators).all()
            for element in elements:
                expect(element).to_be_visible()
        else:
            for locator in locators:
                expect(self.page.locator(locator)).to_be_visible()

    def dropdown_filter(self):
        """Опустить drop-down список 'Фильтры' - изменив параметр элемента в DOM"""
        element = self.page.locator('//*[@id="rootTelemedHub"]/div[2]/main/div/div[2]/div/div')
        element.evaluate('(element) => { element.style.maxHeight = "none"; }')

    def open_dropdown_organization(self):
        """Раскрыть все видимые организации в поле 'Организации' при добавлении пользователя"""
        self.page.click(LocatorsPageUsers.FILTER_DROPDOWN_ORG)
        elements = self.page.locator('//div[@class="arrowControl__e920 arrowControl"]').all()
        col = 0
        while col != len(elements):
            self.click('//div[@class="arrowControl__e920 arrowControl"]')
            col += 1

    def get_quantity_elements(self, locator):
        """Получить количество элементов"""
        elements = self.page.locator(locator).all()
        return len(elements)

    def get_attribute_element(self, locator, type_attribute: str):
        """Получить атрибуты элемента"""
        element = self.page.locator(locator)
        return element.get_attribute(type_attribute)

    def expect_style_element(self, locator, name_style: str, value_style: str):
        """Проверка - 'имя' и 'значение' стиля элемента равны заданным параметрам (name_style, value_style)"""
        element = self.page.locator(locator)
        return expect(element).to_have_css(name_style, value_style)

    def change_password(self, current_pass, new_pass):
        """Смена пароля на стр. /users в профиле пользователя"""
        self.page.fill(LocatorsPageUsers.INPUT_CURRENT_PASS, current_pass)
        self.page.fill(LocatorsPageUsers.INPUT_NEW_PASS, new_pass)
        self.page.fill(LocatorsPageUsers.INPUT_NEW2_PASS, new_pass)

    def expect_invalid_input_color(self, locator_placeholder, locator_body_input):
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

    def clear_inputs(self, locators):
        """Очистить поле ввода"""
        if type(locators) is not list:
            elements = self.page.locator(locators).all()
            for element in elements:
                element.clear()
        else:
            for locator in locators:
                element = self.page.locator(locator)
                element.clear()

    # @staticmethod
    # def api_get_access_token_adm(org_id=100):
    #     """Авторизация под админом определенной организации с последующим получаением токена"""
    #     mail_admin = ''
    #     url = f"http://192.168.7.221:5001/api/v4/Users/Login"
    #     if org_id == 100:
    #         mail_admin = mails_adm[0]
    #     elif org_id == 101:
    #         mail_admin = mails_adm[1]
    #     elif (org_id == 102) or (org_id == 103):
    #         mail_admin = mails_adm[2]
    #     payload = {
    #         "email": mail_admin,
    #         "username": mail_admin,
    #         "password": password_all
    #     }
    #     response = requests.post(url, json=payload)
    #     if response.status_code == 200:
    #         response_json = response.json()
    #         access_token = response_json.get("accessToken")
    #         print(f"Тоекн успешно получен {access_token}")
    #         return str(access_token)
    #     else:
    #         print("Что-то прилетело с запросом.")
    #         print("Статус код:", response.status_code)
    #         print("Доп инфа:", response.text)
    #
    # @staticmethod
    # def api_create_doctor(mail, password, access_token, org_id=100):
    #     """Создание пользователя(doctor) под ролью 'Врач / Телемед.центр'
    #
    #     По умолчанию orgId - 100"""
    #     url = "http://192.168.7.221:5001/api/v4/Users/Register"
    #     payload = {
    #       "firstName": "Тестовт",
    #       "lastName": "Тестовт",
    #       "middleName": "Тестович",
    #       "height": 0,
    #       "weight": 0,
    #       "email": mail,
    #       "password": password,
    #       "phone": "3123123123",
    #       "birthDate": "2001-06-06T12:19:32.884Z",
    #       "sex": "male",
    #       "orgId": org_id,
    #       "role": "doctor",
    #       "id": 0
    #     }
    #     headers = {
    #         "Authorization": f"Bearer {access_token}"
    #     }
    #     response = requests.post(url, json=payload, headers=headers)
    #     if response.status_code == 200:
    #         response_json = response.json()
    #         user_id = response_json.get("id")
    #         print(f"Пользователь c id: {user_id} успешно создан.")
    #         return int(user_id)
    #     else:
    #         print("Что-то прилетело с запросом.")
    #         print("Статус код:", response.status_code)
    #         print("Доп инфа:", response.text)
    #
    # @staticmethod
    # def api_delete_user(id_user: int, access_token):
    #     """Удаление пользователя по id_user"""
    #     url = f"http://192.168.7.221:5001/api/v4/Users({id_user})"
    #     headers = {
    #         "Authorization": f"Bearer {access_token}"
    #     }
    #     response = requests.delete(url, headers=headers)
    #     if response.status_code == 200:
    #         print(f"Пользователь c id: {id_user} успешно удален.")
    #     else:
    #         print("Что-то прилетело с запросом.")
    #         print("Статус код:", response.status_code)
    #         print("Доп инфа:", response.text)





