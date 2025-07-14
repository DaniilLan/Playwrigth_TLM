from page_objects.base_page import BasePage
from page_objects.locators.base_locators import LocatorsBase
from page_objects.page.support import LocatorsSupport


class LocatorsHelp:
    BUTTON_BAC_AUTH = '//div[@class="ArrowBack__ddDr noPrint__ObjZ"][//span[text()="Авторизация"]]'

    TOPIC_HELP_TERMS = '//div[div[strong[text()="Термины, сокращения и определения"]]]'
    TOPIC_HELP_REGISTRATION = '//div[div[strong[text()="Регистрация"]]]'
    TOPIC_HELP_AUTHORIZATION = '//div[div[strong[text()="Авторизация"]]]'
    TOPIC_HELP_PASSWORD_RECOVER = '//div[div[strong[text()="Восстановление пароля"]]]'
    TOPIC_HELP_PROFILE_SETUP = '//div[div[strong[text()="Настройка профиля"]]][1]'
    TOPIC_HELP_ADMIN_APP = '//div[div[strong[text()="Порядок работы администратора в веб-приложении"]]]'
    TOPIC_HELP_DOCTOR_APP = '//div[div[strong[text()="Порядок работы врача в веб-приложении"]]]'

    PANEL_HELP_TERMS = "//strong[text()='Термины, сокращения и определения']/ancestor::div[contains(@class, 'AccordionHelp__RXGy')]//div[contains(@class, 'accordionItem__e235')]"
    PANEL_HELP_REGISTRATION = "//strong[text()='Регистрация']/ancestor::div[contains(@class, 'AccordionHelp__RXGy')]//div[contains(@class, 'accordionItem__e235')]"
    PANEL_HELP_AUTHORIZATION = "//strong[text()='Авторизация']/ancestor::div[contains(@class, 'AccordionHelp__RXGy')]//div[contains(@class, 'accordionItem__e235')]"
    PANEL_HELP_PASSWORD_RECOVER = "//strong[text()='Восстановление пароля']/ancestor::div[contains(@class, 'AccordionHelp__RXGy')]//div[contains(@class, 'accordionItem__e235')]"
    PANEL_HELP_PROFILE_SETUP = "//strong[text()='Настройка профиля']/ancestor::div[contains(@class, 'AccordionHelp__RXGy')]//div[contains(@class, 'accordionItem__e235')]"
    PANEL_HELP_ADMIN_APP = "//strong[text()='Порядок работы администратора в веб-приложении']/ancestor::div[contains(@class, 'AccordionHelp__RXGy')]//div[contains(@class, 'accordionItem__e235')]"
    PANEL_HELP_DOCTOR_APP = "//strong[text()='Порядок работы врача в веб-приложении']/ancestor::div[contains(@class, 'AccordionHelp__RXGy')]//div[contains(@class, 'accordionItem__e235')]"

    BUTTON_USER_MANUAL = '//button[//span[text()="Руководство пользователя"]]'

    LINK_HELP = '//a[text()="Помощь"]'
    LINK_SUPPORTS = '//a[text()="Поддержка"]'

class HelpPage(BasePage):

    def click_on_topic_terms(self):
        self.click(LocatorsHelp.TOPIC_HELP_TERMS)

    def click_on_topic_registration(self):
        self.click(LocatorsHelp.TOPIC_HELP_REGISTRATION)

    def click_on_topic_authorization(self):
        self.click(LocatorsHelp.TOPIC_HELP_AUTHORIZATION)

    def click_on_topic_password_recover(self):
        self.click(LocatorsHelp.TOPIC_HELP_PASSWORD_RECOVER)

    def click_on_topic_profile_setup(self):
        self.click(LocatorsHelp.TOPIC_HELP_PROFILE_SETUP)

    def click_on_topic_help_for_admin(self):
        self.click(LocatorsHelp.TOPIC_HELP_ADMIN_APP)

    def click_on_topic_help_for_doctor(self):
        self.click(LocatorsHelp.TOPIC_HELP_DOCTOR_APP)

    def expect_visible_panel_terms(self):
        self.expect_open_element(LocatorsHelp.PANEL_HELP_TERMS)

    def expect_visible_panel_registration(self):
        self.expect_open_element(LocatorsHelp.PANEL_HELP_REGISTRATION)

    def expect_visible_panel_authorization(self):
        self.expect_open_element(LocatorsHelp.PANEL_HELP_AUTHORIZATION)

    def expect_visible_panel_password_recover(self):
        self.expect_open_element(LocatorsHelp.PANEL_HELP_PASSWORD_RECOVER)

    def expect_visible_panel_profile_setup(self):
        self.expect_open_element(LocatorsHelp.PANEL_HELP_PROFILE_SETUP)

    def expect_visible_panel_help_for_admin(self):
        self.expect_open_element(LocatorsHelp.PANEL_HELP_ADMIN_APP)

    def expect_visible_panel_help_for_doctor(self):
        self.expect_open_element(LocatorsHelp.PANEL_HELP_DOCTOR_APP)

    def click_on_user_manual(self):
        self.expect_url_pdf(self.conf.pdf.user_manual, LocatorsHelp.BUTTON_USER_MANUAL)

    def click_on_link_help(self):
        self.click(LocatorsBase.HELP_LINK)

    def click_on_link_support(self):
        self.click(LocatorsBase.SUPPORTS_LINK)

    def click_on_button_auth(self):
        self.click(LocatorsHelp.BUTTON_BAC_AUTH)

    def expect_valid_go_to_auth_page(self):
        self.expect_url(self.conf.urls.base)

    def expect_valid_click_on_link_help(self):
        self.expect_url(f"{self.conf.urls.base}help")
        self.wait_visible_elements(LocatorsHelp.BUTTON_BAC_AUTH)

    def expect_valid_go_to_support_page(self):
        self.expect_url(f"{self.conf.urls.base}support")
        self.wait_visible_elements(LocatorsSupport.MAIN_DIV_SUPPORT)

    def click_on_logo(self):
        self.click(LocatorsBase.LOGO_SAMGMU)

    def expect_url_is_auth(self):
        self.expect_url(self.conf.urls.base)