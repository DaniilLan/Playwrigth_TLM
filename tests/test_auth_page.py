from tests.config import *
import time
import pytest
import json
from playwright.sync_api import Route
from PageLocators.locators import LocatorsPageAuth, LocatorsGeneral
import re


class TestPageAuth:

    @pytest.mark.parametrize('elements', [LocatorsGeneral.LOGO_SAMGMU,
                                          LocatorsGeneral.YEAR_BOT,
                                          LocatorsPageAuth.INPUT_MAIL,
                                          LocatorsPageAuth.INPUT_PASSWORD,
                                          LocatorsPageAuth.BUTTON_LOG,
                                          LocatorsPageAuth.LINK_FORGOT_PASSWORD,
                                          LocatorsPageAuth.EYE_PASSWORD,
                                          LocatorsPageAuth.PLACEHOLDER_EMAIL,
                                          LocatorsPageAuth.PLACEHOLDER_PASSWORD,
                                          LocatorsGeneral.HELP_LINK,
                                          LocatorsGeneral.SUPPORTS_LINK])
    def test_visible_elements(self, page_auth, elements):
        page_auth.expect_visible_elements(elements)

    @pytest.mark.parametrize("mail, password, expected_error", [
        # Валидная почта + неверный пароль
        (valid_mail, "1278", "Неверный пароль!"),
        # Невалидная почта + любой пароль
        (invalid_mail, "1278", "Имя пользователя или пароль не верные."),
    ], ids=[
        "valid_email_wrong_password",
        "invalid_email_any_password"
    ])
    def test_invalid_auth(self, page_auth, mail, password, expected_error):
        page_auth.fill_text(LocatorsPageAuth.INPUT_MAIL, mail)
        page_auth.fill_text(LocatorsPageAuth.INPUT_PASSWORD, password)
        page_auth.click(LocatorsPageAuth.BUTTON_LOG)
        page_auth.wait_visible_elements(LocatorsGeneral.NOTIFICATION_ALL)
        actual_error = page_auth.get_texts(LocatorsGeneral.NOTIFICATION_ALL)
        assert actual_error == expected_error

    def test_focus_input_mail(self, page_auth):
        page_auth.focus_element(LocatorsPageAuth.INPUT_MAIL)
    
    def test_focus_input_pass(self, page_auth):
        page_auth.focus_element(LocatorsPageAuth.INPUT_PASSWORD)

    def test_placeholder_before_click(self, page_auth):
        page_auth.click(LocatorsPageAuth.INPUT_MAIL)
        page_auth.expect_visible_elements(LocatorsPageAuth.PLACEHOLDER_EMAIL)
        type_class_mail = page_auth.get_attribute_element(LocatorsPageAuth.DIV_INPUT_EMAIL, 'class')
        assert 'focused__e6b9' in type_class_mail
        page_auth.click(LocatorsPageAuth.INPUT_PASSWORD)
        page_auth.expect_visible_elements(LocatorsPageAuth.PLACEHOLDER_PASSWORD)
        type_class_pass = page_auth.get_attribute_element(LocatorsPageAuth.DIV_INPUT_PASS, 'class')
        assert 'focused__e6b9' in type_class_pass

    def test_type_password(self, page_auth):
        page_auth.fill_text(LocatorsPageAuth.INPUT_PASSWORD, "12345678")
        assert page_auth.get_attribute_element(LocatorsPageAuth.INPUT_PASSWORD, 'type') == 'password'

    def test_ear_password(self, page_auth):
        page_auth.fill_text(LocatorsPageAuth.INPUT_PASSWORD, "12345678")
        page_auth.click(LocatorsPageAuth.EYE_PASSWORD)
        assert page_auth.get_attribute_element(LocatorsPageAuth.INPUT_PASSWORD, 'type') == 'text'
        page_auth.click(LocatorsPageAuth.EYE_PASSWORD)
        assert page_auth.get_attribute_element(LocatorsPageAuth.INPUT_PASSWORD, 'type') == 'password'

    def test_color_input_mail(self, page_auth):
        page_auth.click(LocatorsPageAuth.BUTTON_LOG)
        color_text = LocatorsPageAuth.PLACEHOLDER_EMAIL
        border_background_color = LocatorsPageAuth.INPUT_MAIL
        page_auth.expect_invalid_input_color(color_text, border_background_color)

    def test_color_input_password(self, page_auth):
        page_auth.click(LocatorsPageAuth.BUTTON_LOG)
        color_text = LocatorsPageAuth.PLACEHOLDER_PASSWORD
        border_background_color = LocatorsPageAuth.INPUT_PASSWORD
        page_auth.expect_invalid_input_color(color_text, border_background_color)

class TestForgotPassword:

    def test_valid_forgot_password(self, page_auth):
        page_auth.click(LocatorsPageAuth.LINK_FORGOT_PASSWORD)
        page_auth.expect_visible_elements(LocatorsPageAuth.PLACEHOLDER_EMAIL)
        page_auth.fill_text(LocatorsPageAuth.INPUT_MAIL, "landan2001@mail.ru")
        page_auth.click(LocatorsPageAuth.BUTTON_FORGOT)
        page_auth.wait_until_visible_elements(LocatorsGeneral.NOTIFICATION_ALL)

    @pytest.mark.parametrize("mail", ["", invalid_mail],
                             ids=[
                                 "empty_email_forgot_password",
                                 "invalid_email_forgot_password"
                             ])
    def test_forgot_password(self, page_auth, mail):
        page_auth.click(LocatorsPageAuth.LINK_FORGOT_PASSWORD)
        page_auth.expect_visible_elements(LocatorsPageAuth.PLACEHOLDER_EMAIL)
        page_auth.fill_text(LocatorsPageAuth.INPUT_MAIL, mail)
        page_auth.click(LocatorsPageAuth.BUTTON_FORGOT)
        page_auth.wait_visible_elements(LocatorsGeneral.NOTIFICATION_ALL)
        text_notif = page_auth.get_texts(LocatorsGeneral.NOTIFICATION_ALL)
        if mail == '':
            assert text_notif == "Отсутствует обязательное поле email!"
            page_auth.wait_until_visible_elements(LocatorsGeneral.NOTIFICATION_ALL)
        elif mail == invalid_mail:
            assert text_notif == f"Пользователь c логином '{invalid_mail}' не существует!"
            page_auth.wait_until_visible_elements(LocatorsGeneral.NOTIFICATION_ALL)

    def test_cancel_forgot_password(self, page_auth):
        page_auth.click(LocatorsPageAuth.LINK_FORGOT_PASSWORD)
        page_auth.click(LocatorsPageAuth.BUTTON_CANCEL)
        page_auth.expect_visible_elements(LocatorsPageAuth.BUTTON_LOG)

    def test_color_input_mail_forgot(self, page_auth):
        page_auth.click(LocatorsPageAuth.LINK_FORGOT_PASSWORD)
        page_auth.click(LocatorsPageAuth.BUTTON_LOG)
        color_text = LocatorsPageAuth.PLACEHOLDER_EMAIL
        border_background_color = LocatorsPageAuth.INPUT_MAIL
        page_auth.expect_invalid_input_color(color_text, border_background_color)