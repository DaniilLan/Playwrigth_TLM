from tests.config import *
import time
import pytest
import json
from playwright.sync_api import Route
from PageLocators.locators import Locators as Loc
import re


# @pytest.mark.parametrize('url', list_url_test)
# class TestGeneralElements:
#     @staticmethod
#     @pytest.mark.parametrize('elements', [[Loc.LOGO_SAMGMU, Loc.YEAR_BOT, Loc.HELP_LINK, Loc.SUPPORTS_LINK]])
#     def test_general_elements(page_general, elements, url):
#         page_general.open(url)
#         if url is url_users_test:
#             page_general.login_users(page_general, "adm@adm.com", "12345678")
#         page_general.expect_visible_elements(elements)
#
#     @staticmethod
#     @pytest.mark.parametrize('link_element', [Loc.HELP_LINK, Loc.SUPPORTS_LINK])
#     def test_open_link(page_general, link_element, url):
#         if url is not url_users_test:
#             page_general.open(url)
#             page_general.click(link_element)
#             if link_element is Loc.HELP_LINK:
#                 assert page_general.get_url() == url_help_test
#             elif link_element is Loc.SUPPORTS_LINK:
#                 assert page_general.get_url() == url_support_test
#
#
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
#     def test_placeholder_before_click(page_auth):
#         page_auth.click(page_auth.PageAuth.INPUT_MAIL)
#         page_auth.expect_visible_element(page_auth.PageAuth.PLACEHOLDER_EMAIL)
#         type_class_mail = page_auth.get_attribute_element(page_auth.PageAuth.DIV_INPUT_EMAIL, 'class')
#         assert 'focused__e6b9' in type_class_mail
#         page_auth.click(page_auth.PageAuth.INPUT_PASSWORD)
#         page_auth.expect_visible_element(page_auth.PageAuth.PLACEHOLDER_PASSWORD)
#         type_class_pass = page_auth.get_attribute_element(page_auth.PageAuth.DIV_INPUT_PASS, 'class')
#         assert 'focused__e6b9' in type_class_pass

#     @staticmethod
#     def test_type_password(page_auth):
#         page_auth.fill_text(page_auth.PageAuth.INPUT_PASSWORD, "12345678")
#         assert page_auth.get_attribute_element(page_auth.PageAuth.INPUT_PASSWORD, 'type') == 'password'
#
#     @staticmethod
#     def test_ear_password(page_auth):
#         page_auth.fill_text(page_auth.PageAuth.INPUT_PASSWORD, "12345678")
#         page_auth.click(page_auth.PageAuth.EYE_PASSWORD)
#         assert page_auth.get_attribute_element(page_auth.PageAuth.INPUT_PASSWORD, 'type') == 'text'
#         page_auth.click(page_auth.PageAuth.EYE_PASSWORD)
#         assert page_auth.get_attribute_element(page_auth.PageAuth.INPUT_PASSWORD, 'type') == 'password'
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

    # @staticmethod
    # def test_color_input_mail(page_auth):
    #     page_auth.focus_element(page_auth.PageAuth.INPUT_MAIL)
    #     page_auth.click(page_auth.LOGO_SAMGMU)
    #     color_text = page_auth.PageAuth.PLACEHOLDER_EMAIL
    #     border_background_color = page_auth.PageAuth.INPUT_MAIL
    #     page_auth.expect_invalid_input_color(color_text, border_background_color)

    # @staticmethod
    # def test_color_input_password(page_auth):
    #     page_auth.focus_element(page_auth.PageAuth.INPUT_PASSWORD)
    #     page_auth.click(page_auth.LOGO_SAMGMU)
    #     color_text = page_auth.PageAuth.PLACEHOLDER_PASSWORD
    #     border_background_color = page_auth.PageAuth.INPUT_PASSWORD
    #     page_auth.expect_invalid_input_color(color_text, border_background_color)

    # @staticmethod
    # def test_color_input_mail_forgot(page_auth):
    #     page_auth.click(page_auth.PageAuth.LINK_FORGOT_PASSWORD)
    #     page_auth.focus_element(page_auth.PageAuth.INPUT_MAIL)
    #     page_auth.click(page_auth.LOGO_SAMGMU)
    #     color_text = page_auth.PageAuth.PLACEHOLDER_EMAIL
    #     border_background_color = page_auth.PageAuth.INPUT_MAIL
    #     page_auth.expect_invalid_input_color(color_text, border_background_color)

# class TestPageHelp:
#
#     @staticmethod
#     def test_bac_auth_from_help(page_help):
#         page_help.click(page_help.PageHelp.BUTTON_BAC_AUTH)
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
#
#
# class TestPageSupport:
#
#     @staticmethod
#     def test_bac_auth_from_support(page_support):
#         page_support.click(page_support.PageSupport.BUTTON_BAC_AUTH)
#         page_support.expect_visible_element(page_support.PageAuth.BUTTON_LOG)
#
#     @staticmethod
#     def test_mail_link(page_support):
#         mail_link = page_support.PageSupport.LINK_PHONE
#         mail = page_support.get_attribute_element(mail_link, 'href')
#         mail_text = page_support.get_text(mail_link)
#         page_support.click(mail_link)
#         assert mail_text in mail
#
#     @staticmethod
#     def test_phone_link(page_support):
#         phone_link = page_support.PageSupport.LINK_PHONE
#         phone = page_support.get_attribute_element(phone_link, 'href')
#         phone_text = page_support.get_text(phone_link)
#         page_support.click(phone_link)
#         assert phone_text in phone


class TestPageUsers:
#
#     @staticmethod
#     @pytest.mark.parametrize('mail, name', [(mail, name) for mail, name in cred.items()])
#     @pytest.mark.parametrize('password', [password_all])
#     def test_auth(page_users, mail, password, name):
#         page_users.login_users(page_users, mail, password)
#         name_profile = page_users.get_text(page_users.PageUsers.NAME_PROFILE)
#         assert name_profile == name
#         page_users.screenshot(dop=mail)

    # @staticmethod
    # @pytest.mark.parametrize('mail', [mail_doc])
    # @pytest.mark.parametrize('password', [password_all])
    # def test_header_organization(page_users, mail, password):
    #     page_users.login_users(page_users, mail, password)
    #     page_users.click(page_users.PageUsers.BUTTON_HEADER_ALLMS)
    #     page_users.expect_visible_element(page_users.PageAllMeasurements.TEXT_ALL_MEASUREMENTS)
    #
    # @staticmethod
    # @pytest.mark.parametrize('mail', [mail_doc])
    # @pytest.mark.parametrize('password', [password_all])
    # def test_header_meetings(page_users, mail, password):
    #     page_users.login_users(page_users, mail, password)
    #     page_users.click(page_users.PageUsers.BUTTON_HEADER_MEETING)
    #     page_users.expect_visible_element(page_users.PageMeetings.BUTTON_ADD_MEETING)

    # @staticmethod
    # @pytest.mark.parametrize('mail', mail_doc)
    # @pytest.mark.parametrize('password', [password_all])
    # @pytest.mark.parametrize('locator', [Loc.PageUsers.BUTTON_HEADER_USERS,
    #                                      Loc.PageUsers.BUTTON_HEADER_ALLMS,
    #                                      Loc.PageUsers.BUTTON_HEADER_MEETING,
    #                                      Loc.PageUsers.BUTTON_ADD_PATIENT,
    #                                      Loc.PageUsers.BELL])
    # def test_button_role_doc(page_users, mail, password, locator):
    #     page_users.login_users(page_users, mail, password)
    #     page_users.expect_visible_element(locator)
    #
    # @staticmethod
    # @pytest.mark.parametrize('mail', mail_adm)
    # @pytest.mark.parametrize('password', [password_all])
    # @pytest.mark.parametrize('locator', [[Loc.PageUsers.BUTTON_HEADER_USERS,
    #                                      Loc.PageUsers.BUTTON_HEADER_ORGANIZATION,
    #                                      Loc.PageUsers.BUTTON_HEADER_SETTINGS,
    #                                      Loc.PageUsers.BUTTON_LOGS_AUDIT,
    #                                      Loc.PageUsers.BUTTON_LOAD_PATIENT,
    #                                      Loc.PageUsers.BUTTON_ADD_USERS]])
    # def test_button_role_adm(page_users, mail, password, locator):
    #     page_users.login_users(page_users, mail, password)
    #     page_users.expect_visible_elements(locator)

#     @staticmethod
#     @pytest.mark.parametrize('mail', [mail_adm, mail_doc])
#     @pytest.mark.parametrize('password', [password_all])
#     def test_text_(page_users, mail, password):
#         page_users.login_users(page_users, mail, password)
#         if mail in mails_adm:
#             page_users.wait_visible_all()
#             assert "Пользователи" in page_users.get_text(page_users.PageUsers.USERS_OR_PATIENTS)
#         elif mail in mails_doc:
#             page_users.wait_visible_all()
#             assert "Пациенты" in page_users.get_text(page_users.PageUsers.USERS_OR_PATIENTS)
#
#     @staticmethod
#     @pytest.mark.parametrize('mail', [mail for mail in cred])
#     @pytest.mark.parametrize('password', [password_all])
#     def test_quantity_users(page_users, mail, password):
#         page_users.login_users(page_users, mail, password)
#         head_quantity = page_users.get_text(page_users.PageUsers.QUANTITY_USERS_HEADER)
#         top = re.split("(,)", head_quantity)
#         top = top[0].strip('()')
#         pag_quantity = page_users.get_text(page_users.PageUsers.QUANTITY_USERS_PAGINATION)
#         bot = re.split("из ", pag_quantity)
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
    class TestChangePassword:
    #
    #     @staticmethod
    #     @pytest.mark.parametrize('mail', [mail_doc])
    #     @pytest.mark.parametrize('password', [password_all])
    #     @pytest.mark.parametrize('pass1, pass2', [(password_all, invalid_pass)])
    #     def test_change_password(page_users, mail, password, pass1, pass2):
    #         page_users.login_users(page_users, mail, password)
    #         page_users.click(page_users.PageUsers.NAME_PROFILE)
    #         page_users.click(page_users.PageUsers.BUTTON_CHANGE_PASSWORD)
    #         page_users.change_password(page_users, pass1, pass2)
    #         page_users.click(page_users.PageUsers.SAVE_NEW_PASS)
    #         page_users.expect_visible_element(page_users.PageUsers.NOTIFICAL_CHANGE_PASS)
    #         page_users.wait_for_element_visible(page_users.PageUsers.NOTIFICAL_CHANGE_PASS)
    #         page_users.click(page_users.PageUsers.NAME_PROFILE)
    #         page_users.click(page_users.PageUsers.BUTTON_CHANGE_PASSWORD)
    #         page_users.change_password(page_users, pass2, pass1)
    #         page_users.click(page_users.PageUsers.SAVE_NEW_PASS)
    #
        @staticmethod
        @pytest.mark.parametrize('mail', [mail_doc])
        @pytest.mark.parametrize('password', [password_all])
        @pytest.mark.parametrize('body_input', [[Loc.PageUsers.INPUT_CURRENT_PASS,
                                                 Loc.PageUsers.INPUT_NEW_PASS,
                                                 Loc.PageUsers.INPUT_NEW2_PASS]])
        @pytest.mark.parametrize('text_input', [[Loc.PageUsers.PLACEHOLDER_CURRENT_PASS,
                                                 Loc.PageUsers.PLACEHOLDER_NEW_PASS,
                                                 Loc.PageUsers.PLACEHOLDER_NEW2_PASS]])
        def test_color_input_change_password(page_users, mail, password, body_input, text_input):
            page_users.login_users(page_users, mail, password)
            page_users.click(page_users.PageUsers.NAME_PROFILE)
            page_users.click(page_users.PageUsers.BUTTON_CHANGE_PASSWORD)
            page_users.click(page_users.PageUsers.BUTTON_SAVE_NEW_PASS)
            page_users.expect_invalid_input_color(body_input, text_input)
