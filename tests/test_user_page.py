from tests.config import *
import time
import pytest
import json
from playwright.sync_api import Route
from PageLocators.locators import Locators as Loc
import re


class TestPageUsers:

#     @staticmethod
#     @pytest.mark.parametrize('mail, name', [(mail, name) for mail, name in cred.items()])
#     @pytest.mark.parametrize('password', [password_all])
#     def test_auth(page_users, mail, password, name):
#         page_users.login_users(page_users, mail, password)
#         name_profile = page_users.get_text(page_users.PageUsers.NAME_PROFILE)
#         assert name_profile == name
#         page_users.screenshot(dop=mail)
#
#     @staticmethod
#     @pytest.mark.parametrize('mail', [mail_doc])
#     @pytest.mark.parametrize('password', [password_all])
#     def test_header_organization(page_users, mail, password):
#         page_users.login_users(page_users, mail, password)
#         page_users.click(page_users.PageUsers.BUTTON_HEADER_ALLMS)
#         page_users.expect_visible_element(page_users.PageAllMeasurements.TEXT_ALL_MEASUREMENTS)
#
#     @staticmethod
#     @pytest.mark.parametrize('mail', [mail_doc])
#     @pytest.mark.parametrize('password', [password_all])
#     def test_header_meetings(page_users, mail, password):
#         page_users.login_users(page_users, mail, password)
#         page_users.click(page_users.PageUsers.BUTTON_HEADER_MEETING)
#         page_users.expect_visible_element(page_users.PageMeetings.BUTTON_ADD_MEETING)
#
#     @staticmethod
#     @pytest.mark.parametrize('mail', mail_doc)
#     @pytest.mark.parametrize('password', [password_all])
#     @pytest.mark.parametrize('locator', [Loc.PageUsers.BUTTON_HEADER_USERS,
#                                          Loc.PageUsers.BUTTON_HEADER_ALLMS,
#                                          Loc.PageUsers.BUTTON_HEADER_MEETING,
#                                          Loc.PageUsers.BUTTON_ADD_PATIENT,
#                                          Loc.PageUsers.BELL])
#     def test_button_role_doc(page_users, mail, password, locator):
#         page_users.login_users(page_users, mail, password)
#         page_users.expect_visible_element(locator)
#
#     @staticmethod
#     @pytest.mark.parametrize('mail', mail_adm)
#     @pytest.mark.parametrize('password', [password_all])
#     @pytest.mark.parametrize('locator', [[Loc.PageUsers.BUTTON_HEADER_USERS,
#                                          Loc.PageUsers.BUTTON_HEADER_ORGANIZATION,
#                                          Loc.PageUsers.BUTTON_HEADER_SETTINGS,
#                                          Loc.PageUsers.BUTTON_LOGS_AUDIT,
#                                          Loc.PageUsers.BUTTON_LOAD_PATIENT,
#                                          Loc.PageUsers.BUTTON_ADD_USERS]])
#     def test_button_role_adm(page_users, mail, password, locator):
#         page_users.login_users(page_users, mail, password)
#         page_users.expect_visible_elements(locator)
#
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

    # class TestChangePassword:

        # @staticmethod
        # @pytest.mark.parametrize('mail', [mail_lan_doc])
        # @pytest.mark.parametrize('password', [password_all])
        # @pytest.mark.parametrize('new_password', [invalid_pass])
        # def test_valid_change_password(page_users, mail, password, new_password):
        #     create_user_get_id = page_users.api_create_doctor(mail, password_all)
        #     page_users.login_users(page_users, mail, password)
        #     page_users.click(page_users.PageUsers.NAME_PROFILE)
        #     page_users.click(page_users.PageUsers.BUTTON_CHANGE_PASSWORD)
        #     page_users.change_password(page_users, password, new_password)
        #     page_users.click(page_users.PageUsers.BUTTON_SAVE_NEW_PASS)
        #     page_users.wait_for_element_visible(page_users.GeneralLocators.NOTIFICATION)
        #     page_users.api_delete_user(create_user_get_id)

        # @staticmethod
        # @pytest.mark.parametrize('mail', [mail_lan_doc])
        # @pytest.mark.parametrize('password', [password_all])
        # @pytest.mark.parametrize('new_password', [invalid_pass])
        # def test_invalid_without_current_password(page_users, mail, password, new_password):
        #     create_user_get_id = page_users.api_create_doctor(mail, password_all)
        #     page_users.login_users(page_users, mail, password)
        #     page_users.click(page_users.PageUsers.NAME_PROFILE)
        #     page_users.click(page_users.PageUsers.BUTTON_CHANGE_PASSWORD)
        #     page_users.fill_text(page_users.PageUsers.INPUT_NEW_PASS, invalid_pass)
        #     page_users.fill_text(page_users.PageUsers.INPUT_NEW2_PASS, invalid_pass)
        #     page_users.click(page_users.PageUsers.BUTTON_SAVE_NEW_PASS)
        #     page_users.wait_for_element_visible(page_users.GeneralLocators.NOTIFICATION)
        #     page_users.api_delete_user(create_user_get_id)

        # @staticmethod
        # @pytest.mark.parametrize('mail', [mail_lan_doc])
        # @pytest.mark.parametrize('password', [password_all])
        # @pytest.mark.parametrize('new_password', [invalid_pass])
        # def test_invalid_without_re_password(page_users, mail, password, new_password):
        #     create_user_get_id = page_users.api_create_doctor(mail, password_all)
        #     page_users.login_users(page_users, mail, password)
        #     page_users.click(page_users.PageUsers.NAME_PROFILE)
        #     page_users.click(page_users.PageUsers.BUTTON_CHANGE_PASSWORD)
        #     page_users.fill_text(page_users.PageUsers.INPUT_CURRENT_PASS, password_all)
        #     page_users.fill_text(page_users.PageUsers.INPUT_NEW_PASS, invalid_pass)
        #     page_users.click(page_users.PageUsers.BUTTON_SAVE_NEW_PASS)
        #     page_users.wait_for_element_visible(page_users.GeneralLocators.NOTIFICATION)
        #     page_users.api_delete_user(create_user_get_id)


        # @staticmethod
        # @pytest.mark.parametrize('mail', [mail_doc])
        # @pytest.mark.parametrize('password', [password_all])
        # @pytest.mark.parametrize('body_input', [[Loc.PageUsers.INPUT_CURRENT_PASS,
        #                                          Loc.PageUsers.INPUT_NEW_PASS,
        #                                          Loc.PageUsers.INPUT_NEW2_PASS]])
        # @pytest.mark.parametrize('placeholder_input', [[Loc.PageUsers.PLACEHOLDER_CURRENT_PASS,
        #                                                 Loc.PageUsers.PLACEHOLDER_NEW_PASS,
        #                                                 Loc.PageUsers.PLACEHOLDER_NEW2_PASS]])
        # def test_color_input_change_password(page_users, mail, password, body_input, placeholder_input):
        #     page_users.login_users(page_users, mail, password)
        #     page_users.click(page_users.PageUsers.NAME_PROFILE)
        #     page_users.click(page_users.PageUsers.BUTTON_CHANGE_PASSWORD)
        #     page_users.click(page_users.PageUsers.BUTTON_SAVE_NEW_PASS)
        #     page_users.expect_invalid_input_color(placeholder_input, body_input)
        #     page_users.wait_for_element_visible(page_users.GeneralLocators.NOTIFICATION)

    class TestChangeProfile:

        @staticmethod
        @pytest.mark.parametrize('mail', [mail_doc])
        @pytest.mark.parametrize('password', [password_all])
        @pytest.mark.parametrize('body_input', [[Loc.PageUsers.INPUT_CHANGE_F,
                                                 Loc.PageUsers.INPUT_CHANGE_I,
                                                 Loc.PageUsers.INPUT_CHANGE_MAIL,
                                                 Loc.PageUsers.INPUT_CHANGE_PHONE]])
        @pytest.mark.parametrize('placeholder_input', [[Loc.PageUsers.PLACEHOLDER_CHANGE_F,
                                                        Loc.PageUsers.PLACEHOLDER_CHANGE_I,
                                                        Loc.PageUsers.PLACEHOLDER_CHANGE_MAIL,
                                                        Loc.PageUsers.PLACEHOLDER_CHANGE_PHONE]])
        def test_empty_input_change_profile(page_users, mail, password, body_input, placeholder_input):
            page_users.login_users(page_users, mail, password)
            page_users.click(page_users.PageUsers.NAME_PROFILE)
            page_users.click(page_users.PageUsers.BUTTON_CHANGE_PROFILE)
            page_users.clear_inputs(body_input)
            page_users.click(page_users.PageUsers.BUTTON_SAVE_PROFILE)
            page_users.expect_invalid_input_color(placeholder_input, body_input)
            page_users.wait_for_element_visible(page_users.NOTIFICATION)

