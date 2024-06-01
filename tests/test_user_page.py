from tests.config import *
import time
import pytest
import json
from playwright.sync_api import Route
from PageLocators.locators import Locators as Loc
import re


@pytest.mark.parametrize('url', list_url_test)
@pytest.mark.parametrize("password", [password_all])
@pytest.mark.parametrize('elements', [[Loc.LOGO_SAMGMU, Loc.YEAR_BOT, Loc.HELP_LINK, Loc.SUPPORTS_LINK]])
class TestGeneralElements:
    @staticmethod
    def test_general_elements(general_page, elements, url, mail, password):
        general_page.open(url)
        if url is url_users_test:
            general_page.login_users(general_page, "adm@adm.com", "12345678")
        general_page.expect_visible_elements(elements)


# @staticmethod
    # def test_elements_auth(page_auth, elements):
    #     page_auth.expect_visible_elements(elements)
    #
    # @staticmethod
    # def test_elements_help(page_help, elements):
    #     page_help.expect_visible_elements(elements)
    #
    # @staticmethod
    # def test_elements_support(page_support, elements):
    #     page_support.expect_visible_elements(elements)
    #
    # @staticmethod
    # @pytest.mark.parametrize("mail", ["adm@adm.com", "doc@doc.com"])
    # @pytest.mark.parametrize("password", [password_all])
    # def test_elements_users(page_users, elements, mail, password):
    #     page_users.login_users(page_users, mail, password)
    #     page_users.expect_visible_elements(elements)


# class TestPageAuth:
#
#     @staticmethod
#     @pytest.mark.parametrize('elements', [Loc.LOGO_SAMGMU,
#                                           Loc.YEAR_BOT,
#                                           Loc.PageAuth.INPUT_MAIL,
#                                           Loc.PageAuth.INPUT_PASSWORD,
#                                           Loc.PageAuth.BUTTON_LOG,
#                                           Loc.PageAuth.FORGOT_PASSWORD,
#                                           Loc.PageAuth.EYE_PASSWORD,
#                                           Loc.PageAuth.PLACEHOLDER_EMAIL,
#                                           Loc.PageAuth.PLACEHOLDER_PASSWORD,
#                                           Loc.HELP_LINK,
#                                           Loc.SUPPORTS_LINK])
#     def test_visible_elements(page_auth, elements):
#         page_auth.expect_visible_element(elements)
#
#     @staticmethod
#     def test_focus_input(page_auth):
#         page_auth.focus_element(page_auth.PageAuth.INPUT_MAIL)
#         page_auth.focus_element(page_auth.PageAuth.INPUT_PASSWORD)
#
#     @staticmethod
#     def test_visible_placeholder_before_click(page_auth):
#         page_auth.click(page_auth.PageAuth.INPUT_MAIL)
#         page_auth.expect_visible_element(page_auth.PageAuth.PLACEHOLDER_EMAIL)
#         page_auth.click(page_auth.PageAuth.INPUT_PASSWORD)
#         page_auth.expect_visible_element(page_auth.PageAuth.PLACEHOLDER_PASSWORD)
#
#     @staticmethod
#     def test_type_password(page_auth):
#         page_auth.fill_text(page_auth.PageAuth.INPUT_PASSWORD, "12345678")
#         assert page_auth.get_type_element(page_auth.PageAuth.INPUT_PASSWORD) == 'password'
#
#     @staticmethod
#     def test_ear_password(page_auth):
#         page_auth.fill_text(page_auth.PageAuth.INPUT_PASSWORD, "12345678")
#         page_auth.click(page_auth.PageAuth.EYE_PASSWORD)
#         assert page_auth.get_type_element(page_auth.PageAuth.INPUT_PASSWORD) == 'text'
#         page_auth.click(page_auth.PageAuth.EYE_PASSWORD)
#         assert page_auth.get_type_element(page_auth.PageAuth.INPUT_PASSWORD) == 'password'
#
#     @staticmethod
#     def test_forgot_password(page_auth):
#         page_auth.click(page_auth.PageAuth.FORGOT_PASSWORD)
#         page_auth.expect_visible_element(page_auth.PageAuth.PLACEHOLDER_EMAIL)
#         page_auth.fill_text(page_auth.PageAuth.INPUT_MAIL, "landan2001@mail.ru")
#         page_auth.click(page_auth.PageAuth.BUTTON_FORGOT)
#         page_auth.expect_visible_element(page_auth.PageAuth.NOTIFICATION_FORGOT_PASSWORD)
#
#     @staticmethod
#     def test_cancel_forgot_password(page_auth):
#         page_auth.click(page_auth.PageAuth.FORGOT_PASSWORD)
#         page_auth.click(page_auth.PageAuth.BUTTON_CANCEL)
#         page_auth.expect_visible_element(page_auth.PageAuth.BUTTON_LOG)
#
#
# class TestPageHelp:
#
#     @staticmethod
#     def test_bac_auth_from_help(page_help):
#         page_help.click(page_help.PageAuth.BUTTON_BAC_AUTH)
#         page_help.expect_visible_element(page_help.PageAuth.BUTTON_LOG)
#
#     @staticmethod
#     @pytest.mark.parametrize('panel_help, open_panel_help', [(panel_help, open_panel_help)
#                                                              for panel_help, open_panel_help
#                                                              in {Loc.PageHelp.PANEL1_HELP: Loc.PageHelp.OPEN_PANEL1_HELP,
#                                                                  Loc.PageHelp.PANEL2_HELP: Loc.PageHelp.OPEN_PANEL2_HELP,
#                                                                  Loc.PageHelp.PANEL3_HELP: Loc.PageHelp.OPEN_PANEL3_HELP,
#                                                                  Loc.PageHelp.PANEL4_HELP: Loc.PageHelp.OPEN_PANEL4_HELP,
#                                                                  Loc.PageHelp.PANEL5_HELP: Loc.PageHelp.OPEN_PANEL5_HELP,
#                                                                  Loc.PageHelp.PANEL6_HELP: Loc.PageHelp.OPEN_PANEL6_HELP,
#                                                                  Loc.PageHelp.PANEL7_HELP: Loc.PageHelp.OPEN_PANEL7_HELP}.items()])
#     def test_open_panels_help(page_help, panel_help, open_panel_help):
#         page_help.click(panel_help)
#         page_help.expect_visible_element(open_panel_help)

class TestPageSupport:

    @staticmethod
    def test_bac_auth_from_help(page_support):
        page_support.click(page_support.PageSupport.BUTTON_BAC_AUTH)
        page_support.expect_visible_element(page_support.PageAuth.BUTTON_LOG)
















# class TestPageUsers:
#
#     @staticmethod
#     @pytest.mark.parametrize('mail, name', [(mail, name) for mail, name in cred.items()])
#     @pytest.mark.parametrize('password', [password_all])
#     def test_auth(page, mail, password, name):
#         page.login_users(page, mail, password)
#         page.expect_visible_element(page.PageUsers.NAME_PROFILE)
#         page.screenshot(dop=mail)

#     @staticmethod
#     @pytest.mark.parametrize('mail', mails_doc)
#     @pytest.mark.parametrize('password', [password_all])
#     @pytest.mark.parametrize('locator', [Loc.PageUsers.BUTTON_HEADER_USERS,
#                                          Loc.PageUsers.BUTTON_HEADER_ALLMS,
#                                          Loc.PageUsers.BUTTON_HEADER_MEETING,
#                                          Loc.PageUsers.BUTTON_ADD_PATIENT,
#                                          Loc.PageUsers.BELL])
#     def test_button_role_doc(page, mail, password, locator):
#         page.login_users(page, mail, password)
#         page.expect_visible_element(locator)
#
#     @staticmethod
#     @pytest.mark.parametrize('mail', mails_adm)
#     @pytest.mark.parametrize('password', [password_all])
#     @pytest.mark.parametrize('locator', [PageUsers.BUTTON_HEADER_USERS,
#                                          Loc.PageUsers.BUTTON_HEADER_ORGANIZATION,
#                                          Loc.PageUsers.BUTTON_HEADER_SETTINGS,
#                                          Loc.PageUsers.BUTTON_LOGS_AUDIT,
#                                          Loc.PageUsers.BUTTON_LOAD_PATIENT,
#                                          Loc.PageUsers.BUTTON_ADD_USERS])
#     def test_button_role_adm(page, mail, password, locator):
#         page.login_users(page, mail, password)
#         page.expect_visible_element(locator)
#
#     @staticmethod
#     @pytest.mark.parametrize('mail', [mail for mail in cred])
#     @pytest.mark.parametrize('password', [password_all])
#     def test_text_(page, mail, password):
#         page.login_users(page, mail, password)
#         if mail in mails_adm:
#             page.wait_visible_all()
#             assert "Пользователи" in page.get_text(page.PageUsers.USERS_OR_PATIENTS)
#         elif mail in mails_doc:
#             page.wait_visible_all()
#             assert "Пациенты" in page.get_text(page.PageUsers.USERS_OR_PATIENTS)
#
#     @staticmethod
#     @pytest.mark.parametrize('mail', [mail for mail in cred])
#     @pytest.mark.parametrize('password', [password_all])
#     def test_quantity_users(page, mail, password):
#         page.login_users(page, mail, password)
#         head_quantity = page.get_text(page.PageUsers.QUANTITY_USERS_HEADER)
#         top = re.split("(,)", head_quantity)
#         top = top[0].strip('()')
#         pag_quantity = page.get_text(page.PageUsers.QUANTITY_USERS_PAGINATION)
#         bot = re.split("из ", pag_quantity)
#         print(top, bot[1])
#         assert bot[1] in top
#
#     @staticmethod
#     @pytest.mark.parametrize('mail', [mail for mail in cred])
#     @pytest.mark.parametrize('password', [password_all])
#     def test_drop_filter(page, mail, password):
#         page.login_users(page, mail, password)
#         page.click(page.DROPDOWN_FILTER)
#
#     @staticmethod
#     @pytest.mark.parametrize('mail', [mail for mail in cred])
#     @pytest.mark.parametrize('password', [password_all])
#     def test_boxs_input_filter(page, mail, password):
#         page.login_users(page, mail, password)
#         page.dropdown_filter()
#         page.click_on_elements(page.PageUsers.FILTER_INPUT_BOXS)
#
#     @staticmethod
#     @pytest.mark.parametrize('mail', [mail for mail in cred])
#     @pytest.mark.parametrize('password', [password_all])
#     def test_boxs_dropdown_filter(page, mail, password):
#         page.login_users(page, mail, password)
#         page.dropdown_filter()
#         page.click(page.PageUsers.FILTER_DROPDOWN_GENDER)
#         page.click(page.PageUsers.FILTER_DROPDOWN_ORGANIZATION)
#         if mail in mails_adm:
#             page.click(page.PageUsers.FILTER_DROPDOWN_ROLE)
#
#
# @pytest.mark.parametrize('mail', [mail for mail in mails_doc])
# @pytest.mark.parametrize('password', [password_all])
# class TestPagination:
#
#     @staticmethod
#     @pytest.mark.parametrize('limit', [Loc.PageUsers.PAGINATION_20,
#                                        Loc.PageUsers.PAGINATION_50,
#                                        Loc.PageUsers.PAGINATION_100,
#                                        Loc.PageUsers.PAGINATION_150])
#     def test_quantity_user_limit(page, limit, mail, password):
#         page.login_users(page, mail, password)
#         page.click(limit)
#         quantity_pagination = page.get_text(limit)
#         quantity_users = page.get_quantity_elements(page.PageUsers.USERS_LIST)
#         assert quantity_users == int(quantity_pagination)
#         page.click(page.PageUsers.BUTTON_HEADER_ALLMS)
#
#
#
#
