from tests.config import *
import time
import pytest
import json
from playwright.sync_api import Route
from PageLocators.locators import Locators as Loc
import re


class TestPageAuth:

    @staticmethod
    @pytest.mark.parametrize('elements', [Loc.GeneralLocators.LOGO_SAMGMU,
                                          Loc.GeneralLocators.YEAR_BOT,
                                          Loc.PageAuth.INPUT_MAIL,
                                          Loc.PageAuth.INPUT_PASSWORD,
                                          Loc.PageAuth.BUTTON_LOG,
                                          Loc.PageAuth.LINK_FORGOT_PASSWORD,
                                          Loc.PageAuth.EYE_PASSWORD,
                                          Loc.PageAuth.PLACEHOLDER_EMAIL,
                                          Loc.PageAuth.PLACEHOLDER_PASSWORD,
                                          Loc.GeneralLocators.HELP_LINK,
                                          Loc.GeneralLocators.SUPPORTS_LINK])
    def test_visible_elements(page_auth, elements):
        page_auth.expect_visible_elements(elements)

    @staticmethod
    @pytest.mark.parametrize("mail", [valid_mail, "", invalid_mail])
    @pytest.mark.parametrize("password", ["", "123123", ])
    def test_invalid_auth(page_auth, mail, password):
        page_auth.fill_text(page_auth.PageAuth.INPUT_MAIL, mail)
        page_auth.fill_text(page_auth.PageAuth.INPUT_PASSWORD, password)
        page_auth.click(page_auth.PageAuth.BUTTON_LOG)
        page_auth.wait_visible_elements(page_auth.GeneralLocators.NOTIFICATION_ALL)
        text_notif = page_auth.get_texts(page_auth.GeneralLocators.NOTIFICATION_ALL)
        if (password == '') and (mail != ''):
            print(text_notif)
            assert text_notif == "Заполните полe 'Пароль'"
            page_auth.wait_until_visible_elements(page_auth.GeneralLocators.NOTIFICATION_ALL)
        elif (password != '') and (mail == ''):
            print(text_notif)
            assert text_notif == "Заполните полe 'E-mail'"
            page_auth.wait_until_visible_elements(page_auth.GeneralLocators.NOTIFICATION_ALL)
        elif (password == '') and (mail == ''):
            print(text_notif)
            assert text_notif == "Заполните полe 'E-mail'Заполните полe 'Пароль'"
            page_auth.wait_until_visible_elements(page_auth.GeneralLocators.NOTIFICATION_ALL)
        elif (mail == valid_mail) and (password != ''):
            print(text_notif)
            assert text_notif == "Неверный пароль!"
            page_auth.wait_until_visible_elements(page_auth.GeneralLocators.NOTIFICATION_ALL)
        elif (mail == invalid_mail) and (password == "123123"):
            print(text_notif)
            assert text_notif == "Имя пользователя или пароль не верные."
            page_auth.wait_until_visible_elements(page_auth.GeneralLocators.NOTIFICATION_ALL)

    @staticmethod
    def test_focus_input(page_auth):
        page_auth.focus_element(page_auth.PageAuth.INPUT_MAIL)
        page_auth.focus_element(page_auth.PageAuth.INPUT_PASSWORD)

    @staticmethod
    def test_placeholder_before_click(page_auth):
        page_auth.click(page_auth.PageAuth.INPUT_MAIL)
        page_auth.expect_visible_elements(page_auth.PageAuth.PLACEHOLDER_EMAIL)
        type_class_mail = page_auth.get_attribute_element(page_auth.PageAuth.DIV_INPUT_EMAIL, 'class')
        assert 'focused__e6b9' in type_class_mail
        page_auth.click(page_auth.PageAuth.INPUT_PASSWORD)
        page_auth.expect_visible_elements(page_auth.PageAuth.PLACEHOLDER_PASSWORD)
        type_class_pass = page_auth.get_attribute_element(page_auth.PageAuth.DIV_INPUT_PASS, 'class')
        assert 'focused__e6b9' in type_class_pass

    @staticmethod
    def test_type_password(page_auth):
        page_auth.fill_text(page_auth.PageAuth.INPUT_PASSWORD, "12345678")
        assert page_auth.get_attribute_element(page_auth.PageAuth.INPUT_PASSWORD, 'type') == 'password'

    @staticmethod
    def test_ear_password(page_auth):
        page_auth.fill_text(page_auth.PageAuth.INPUT_PASSWORD, "12345678")
        page_auth.click(page_auth.PageAuth.EYE_PASSWORD)
        assert page_auth.get_attribute_element(page_auth.PageAuth.INPUT_PASSWORD, 'type') == 'text'
        page_auth.click(page_auth.PageAuth.EYE_PASSWORD)
        assert page_auth.get_attribute_element(page_auth.PageAuth.INPUT_PASSWORD, 'type') == 'password'

    @staticmethod
    def test_color_input_mail(page_auth):
        page_auth.focus_element(page_auth.PageAuth.INPUT_MAIL)
        page_auth.click(page_auth.GeneralLocators.LOGO_SAMGMU)
        color_text = page_auth.PageAuth.PLACEHOLDER_EMAIL
        border_background_color = page_auth.PageAuth.INPUT_MAIL
        page_auth.expect_invalid_input_color(color_text, border_background_color)

    @staticmethod
    def test_color_input_password(page_auth):
        page_auth.focus_element(page_auth.PageAuth.INPUT_PASSWORD)
        page_auth.click(page_auth.GeneralLocators.LOGO_SAMGMU)
        color_text = page_auth.PageAuth.PLACEHOLDER_PASSWORD
        border_background_color = page_auth.PageAuth.INPUT_PASSWORD
        page_auth.expect_invalid_input_color(color_text, border_background_color)

    class TestForgotPassword:

        @staticmethod
        def test_valid_forgot_password(page_auth):
            page_auth.click(page_auth.PageAuth.LINK_FORGOT_PASSWORD)
            page_auth.expect_visible_elements(page_auth.PageAuth.PLACEHOLDER_EMAIL)
            page_auth.fill_text(page_auth.PageAuth.INPUT_MAIL, "landan2001@mail.ru")
            page_auth.click(page_auth.PageAuth.BUTTON_FORGOT)
            page_auth.wait_until_visible_elements(page_auth.GeneralLocators.NOTIFICATION_FIRS)

        @staticmethod
        @pytest.mark.parametrize("mail", ["", invalid_mail])
        def test_invalid_forgot_password(page_auth, mail):
            page_auth.click(page_auth.PageAuth.LINK_FORGOT_PASSWORD)
            page_auth.expect_visible_elements(page_auth.PageAuth.PLACEHOLDER_EMAIL)
            page_auth.fill_text(page_auth.PageAuth.INPUT_MAIL, mail)
            page_auth.click(page_auth.PageAuth.BUTTON_FORGOT)
            page_auth.wait_visible_elements(page_auth.GeneralLocators.NOTIFICATION_ALL)
            text_notif = page_auth.get_texts(page_auth.GeneralLocators.NOTIFICATION_ALL)
            if mail == '':
                print(text_notif)
                assert text_notif == "Заполните полe 'E-mail'"
                page_auth.wait_until_visible_elements(page_auth.GeneralLocators.NOTIFICATION_ALL)
            elif mail == invalid_mail:
                print(text_notif)
                assert text_notif == f"Пользователь c логином '{invalid_mail}' не существует!"
                page_auth.wait_until_visible_elements(page_auth.GeneralLocators.NOTIFICATION_ALL)

        @staticmethod
        def test_cancel_forgot_password(page_auth):
            page_auth.click(page_auth.PageAuth.LINK_FORGOT_PASSWORD)
            page_auth.click(page_auth.PageAuth.BUTTON_CANCEL)
            page_auth.expect_visible_elements(page_auth.PageAuth.BUTTON_LOG)

        @staticmethod
        def test_color_input_mail_forgot(page_auth):
            page_auth.click(page_auth.PageAuth.LINK_FORGOT_PASSWORD)
            page_auth.focus_element(page_auth.PageAuth.INPUT_MAIL)
            page_auth.click(page_auth.GeneralLocators.LOGO_SAMGMU)
            color_text = page_auth.PageAuth.PLACEHOLDER_EMAIL
            border_background_color = page_auth.PageAuth.INPUT_MAIL
            page_auth.expect_invalid_input_color(color_text, border_background_color)

