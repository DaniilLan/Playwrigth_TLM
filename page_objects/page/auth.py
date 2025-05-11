from typing import Union, List

from playwright.async_api import Page
from page_objects.base_page import BasePage
from page_objects.locators.base_locators import LocatorsBase
from page_objects.page.help import LocatorsHelp
from page_objects.page.support import LocatorsSupport
from page_objects.page.user import LocatorsUsers

import re


class LocatorsAuth:
    INPUT_MAIL = '//*[@id="rootTelemedHub"]/div[2]/main/div/form/div[1]/div[1]/div/input'
    INPUT_PASSWORD = '//*[@id="rootTelemedHub"]/div[2]/main/div/form/div[1]/div[2]/div/input'
    BUTTON_LOGIN = '//*[@id="rootTelemedHub"]/div[2]/main/div/form/div[2]/button'
    PLACEHOLDER_PASSWORD = '//label[text()="Пароль"]'
    PLACEHOLDER_EMAIL = '//label[text()="Email"]'
    LINK_FORGOT_PASSWORD = 'span[data-locator="forgotPassword"]'
    EYE_PASSWORD = 'svg[xmlns="http://www.w3.org/2000/svg"]'
    BUTTON_RESET = '//button[@data-locator="reset"]'
    BUTTON_CANCEL = '//span[text()="Отмена"]'
    DIV_INPUT_EMAIL = '//*[@id="rootTelemedHub"]/div[2]/main/div/form/div[1]/div[1]'
    DIV_INPUT_PASS = '//*[@id="rootTelemedHub"]/div[2]/main/div/form/div[1]/div[2]'
    POP_UP_REQUIRED_INPUT_PASSWORD = "//div[contains(@class, 'InputBody')][.//input[@type='password']]//div[text()='Обязательное поле']"
    POP_UP_REQUIRED_INPUT_MAIL = "//div[contains(@class, 'InputBody')][.//input[@class='Input']]//div[text()='Обязательное поле']"


    auth_elements = [INPUT_MAIL,
                     INPUT_PASSWORD,
                     BUTTON_LOGIN,
                     LINK_FORGOT_PASSWORD,
                     EYE_PASSWORD,
                     PLACEHOLDER_EMAIL,
                     PLACEHOLDER_PASSWORD]


class AuthPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def input_invalid_mail(self):
        mail = self.conf.creds.invalid_mail
        self.fill_text(LocatorsAuth.INPUT_MAIL, mail)
        return mail

    def input_admin_tele(self):
        mail = self.conf.creds.admin_tele
        self.fill_text(LocatorsAuth.INPUT_MAIL, mail)
        name_profile = self.conf.email_name_mapping
        return name_profile[mail]

    def input_admin_amb(self):
        mail = self.conf.creds.admin_amb
        self.fill_text(LocatorsAuth.INPUT_MAIL, mail)
        name_profile = self.conf.email_name_mapping
        return name_profile[mail]

    def input_admin_crb(self):
        mail = self.conf.creds.admin_crb
        self.fill_text(LocatorsAuth.INPUT_MAIL, mail)
        name_profile = self.conf.email_name_mapping
        return name_profile[mail]

    def input_doctor_tele(self):
        mail = self.conf.creds.doctor_tele
        self.fill_text(LocatorsAuth.INPUT_MAIL, mail)
        name_profile = self.conf.email_name_mapping
        return name_profile[mail]

    def input_doctor_amb(self):
        mail = self.conf.creds.doctor_amb
        self.fill_text(LocatorsAuth.INPUT_MAIL, mail)
        name_profile = self.conf.email_name_mapping
        return name_profile[mail]

    def input_doctor_crb(self):
        mail = self.conf.creds.doctor_crb
        self.fill_text(LocatorsAuth.INPUT_MAIL, mail)
        name_profile = self.conf.email_name_mapping
        return name_profile[mail]

    def input_valid_password(self):
        self.fill_text(LocatorsAuth.INPUT_PASSWORD, self.conf.creds.password_valid)

    def input_invalid_password(self):
        self.fill_text(LocatorsAuth.INPUT_PASSWORD, self.conf.creds.password_invalid)

    def click_log_in(self):
        self.click(LocatorsAuth.BUTTON_LOGIN)

    def expect_valid_auth(self, name_profile):
        self.wait_visible_elements(LocatorsUsers.NAME_PROFILE)
        self.expect_text(LocatorsUsers.NAME_PROFILE, name_profile)

    def expect_error_invalid_password(self):
        self.wait_visible_elements(LocatorsBase.NOTIFICATION_ALL)
        self.expect_text(LocatorsBase.NOTIFICATION_ALL, self.conf.error.invalid_password)

    def expect_error_invalid_mail(self):
        self.wait_visible_elements(LocatorsBase.NOTIFICATION_ALL)
        self.expect_text(LocatorsBase.NOTIFICATION_ALL, self.conf.error.invalid_mail)

    def expect_visible_all_elements(self):
        self.wait_visible_elements(LocatorsBase.base_elements)
        self.wait_visible_elements(LocatorsAuth.auth_elements)

    def expect_reducing_placeholder_mail(self):
        placeholder_mail = LocatorsAuth.PLACEHOLDER_EMAIL
        self.expect_css_style(placeholder_mail, "font-size", "15px")
        self.click(placeholder_mail)
        self.expect_css_style(placeholder_mail, "font-size", "12px")

    def expect_reducing_placeholder_password(self):
        placeholder_password = LocatorsAuth.PLACEHOLDER_PASSWORD
        self.expect_css_style(placeholder_password, "font-size", "15px")
        self.click(placeholder_password)
        self.expect_css_style(placeholder_password, "font-size", "12px")

    def click_eye_password(self):
        self.click(LocatorsAuth.EYE_PASSWORD)

    def expect_input_password_is_text(self):
        assert self.get_attribute_element(LocatorsAuth.INPUT_PASSWORD, 'type') == 'text'

    def expect_input_password_is_password(self):
        assert self.get_attribute_element(LocatorsAuth.INPUT_PASSWORD, 'type') == 'password'

    def expect_color_input_mail_is_red(self):
        color_text = LocatorsAuth.PLACEHOLDER_EMAIL
        border_background_color = LocatorsAuth.INPUT_MAIL
        self.expect_invalid_input_color(color_text, border_background_color)

    def expect_color_input_password_is_red(self):
        color_text = LocatorsAuth.PLACEHOLDER_PASSWORD
        border_background_color = LocatorsAuth.INPUT_PASSWORD
        self.expect_invalid_input_color(color_text, border_background_color)

    def click_on_link_forgot_password(self):
        self.click(LocatorsAuth.LINK_FORGOT_PASSWORD)
        self.wait_visible_elements(LocatorsAuth.BUTTON_RESET)

    def input_mail_for_forgot_password(self):
        mail = self.conf.creds.doctor_tele
        self.fill_text(LocatorsAuth.INPUT_MAIL, mail)
        return mail

    def click_on_reset_password(self):
        self.click(LocatorsAuth.BUTTON_RESET)
        self.expect_visible_elements(LocatorsAuth.BUTTON_RESET)

    def expect_notification_valid_reset(self, mail):
        notification = LocatorsBase.NOTIFICATION_ALL
        self.wait_visible_elements(notification)
        self.expect_text(notification, f'Письмо отправлено на почту {mail}')
        self.expect_not_visible_elements(LocatorsAuth.BUTTON_RESET)

    def expect_notification_invalid_reset(self, mail=''):
        notification = LocatorsBase.NOTIFICATION_ALL
        self.wait_visible_elements(notification)
        if mail == '':
            self.expect_text(notification, 'Отсутствует обязательное поле email!')
        elif not re.fullmatch(r'[^@]+@[a-zA-Z]{2}\.[a-zA-Z]{2}', mail):
            self.expect_text(notification, f"Пользователь c логином '{mail}' не существует!")
        else:
            raise AssertionError(f"Невалидный еmail прошел валидацию/верификацию: {mail}")

    def click_cancel_forgot_password(self):
        self.click(LocatorsAuth.BUTTON_CANCEL)
        self.wait_visible_elements(LocatorsAuth.BUTTON_LOGIN)

    def hovering_on_input_field_mail(self):
        self.hovering_on_element(LocatorsAuth.INPUT_MAIL)

    def expect_visible_pop_up_required_password(self):
        self.wait_visible_elements(LocatorsAuth.POP_UP_REQUIRED_INPUT_PASSWORD)

    def expect_visible_pop_up_required_email(self):
        self.wait_visible_elements(LocatorsAuth.POP_UP_REQUIRED_INPUT_MAIL)

    def hovering_on_input_field_password(self):
        self.hovering_on_element(LocatorsAuth.INPUT_PASSWORD)

    def click_on_link_help(self):
        self.click(LocatorsBase.HELP_LINK)

    def click_on_link_support(self):
        self.click(LocatorsBase.SUPPORTS_LINK)

    def expect_valid_go_to_help_page(self):
        self.expect_url(f"{self.conf.urls.base}help")
        self.wait_visible_elements(LocatorsHelp.BUTTON_BAC_AUTH)

    def expect_valid_go_to_support_page(self):
        self.expect_url(f"{self.conf.urls.base}support")
        self.wait_visible_elements(LocatorsSupport.MAIN_DIV_SUPPORT)

    def click_on_logo(self):
        self.click(LocatorsBase.LOGO_SAMGMU)

    def expect_url_is_auth(self):
        self.expect_url(self.conf.urls.base)
