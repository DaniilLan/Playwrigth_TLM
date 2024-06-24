import re
import time

import requests
from playwright.sync_api import expect, Page
import inspect
import json
import pytest
from tests.config import *
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


class MethodsPageUsers:

    def __init__(self, page: Page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def get_url(self):
        return self.page.url

    def click(self, locator):
        self.page.click(locator)

    def click_on_elements(self, locator):
        elements = self.page.locator(locator).all()
        for element in elements:
            time.sleep(1)
            element.click()

    def fill_text(self, locator, value):
        element = self.page.locator(locator)
        expect(element).to_be_visible()
        self.page.fill(locator, value)

    def focus_element(self, locator):
        locator = self.page.locator(locator)
        locator.focus()

    def get_text(self, locator):
        return self.page.text_content(locator, strict=False)

    def wait_load_page(self):
        self.page.wait_for_load_state("domcontentloaded")

    def wait_visible_all(self):
        all_elements = self.page.query_selector_all("*")
        for element in all_elements:
            element.is_visible()

    def wait_for_element_visible(self, selector):
        try:
            self.page.wait_for_selector(selector, state='hidden')
        except PlaywrightTimeoutError:
            print(2)

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

    def login_users(self, page, mail, password):
        self.page.fill(page.PageAuth.INPUT_MAIL, mail)
        self.page.fill(page.PageAuth.INPUT_PASSWORD, password)
        self.page.click(page.PageAuth.BUTTON_LOG)

    def expect_visible_elements(self, locators):
        if type(locators) is not list:
            elements = self.page.locator(locators).all()
            for element in elements:
                expect(element).to_be_visible()
        else:
            for locator in locators:
                self.expect_visible_element(locator)

    def dropdown_filter(self):
        element = self.page.locator('//*[@id="rootTelemedHub"]/div[2]/main/div/div[2]/div[1]/div/div')
        element.evaluate('(element) => { element.style.maxHeight = "none"; }')

    def get_quantity_elements(self, locator):
        elements = self.page.locator(locator).all()
        return len(elements)

    def get_list_elements(self, locator):
        return self.page.locator(locator).all()

    def get_attribute_element(self, locator, type_attribute: str):
        element = self.page.locator(locator)
        return element.get_attribute(type_attribute)

    def expect_style_element(self, locator, name_style: str, value_style: str):
        element = self.page.locator(locator)
        return expect(element).to_have_css(name_style, value_style)

    def change_password(self, page, current_pass, new_pass):
        self.page.fill(page.PageUsers.INPUT_CURRENT_PASS, current_pass)
        self.page.fill(page.PageUsers.INPUT_NEW_PASS, new_pass)
        self.page.fill(page.PageUsers.INPUT_NEW2_PASS, new_pass)

    def expect_invalid_input_color(self, locator_placeholder, locator_body_input):
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
        if type(locators) is not list:
            elements = self.page.locator(locators).all()
            for element in elements:
                element.clear()
        else:
            for locator in locators:
                element = self.page.locator(locator)
                element.clear()

    @staticmethod
    def api_get_access_token_adm():
        url = f"http://192.168.7.221:5001/api/v4/Users/Login"
        payload = {
            "email": mail_adm,
            "username": mail_adm,
            "password": password_all
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            response_json = response.json()
            access_token = response_json.get("accessToken")
            print(f"Тоекн успешно получен {access_token}")
            return str(access_token)
        else:
            print("Что-то прилетело с запросом.")
            print("Статус код:", response.status_code)
            print("Доп инфа:", response.text)

    access_token = api_get_access_token_adm()

    @staticmethod
    def api_create_doctor(mail, password, access_token=access_token):
        url = "http://192.168.7.221:5001/api/v4/Users/Register"
        payload = {
          "firstName": "Тестовт",
          "lastName": "Тестовт",
          "middleName": "Тестович",
          "height": 0,
          "weight": 0,
          "email": mail,
          "password": password,
          "phone": "3123123123",
          "birthDate": "2001-06-06T12:19:32.884Z",
          "sex": "male",
          "orgId": 100,
          "role": "doctor",
          "id": 0
        }
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            response_json = response.json()
            user_id = response_json.get("id")
            print(f"Пользователь c id: {user_id} успешно создан.")
            return int(user_id)
        else:
            print("Что-то прилетело с запросом.")
            print("Статус код:", response.status_code)
            print("Доп инфа:", response.text)

    # @staticmethod
    # def api_create_admin(mail, password, access_token):
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
    #       "orgId": 100,
    #       "role": "admin",
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

    @staticmethod
    def api_delete_user(id_user: int, access_token=access_token):
        url = f"http://192.168.7.221:5001/api/v4/Users({id_user})"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.delete(url, headers=headers)
        if response.status_code == 200:
            print(f"Пользователь c id: {id_user} успешно удален.")
        else:
            print("Что-то прилетело с запросом.")
            print("Статус код:", response.status_code)
            print("Доп инфа:", response.text)
