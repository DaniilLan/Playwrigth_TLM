from tests.config import *
import time
import pytest
from conftest import *
import json
from playwright.sync_api import Route
from PageLocators.locators import Locators as Loc
import re


class TestPageUsers:

    @staticmethod
    @pytest.mark.parametrize('mail', [mail_lan_doc])
    @pytest.mark.parametrize('password', [password_all])
    def test_header_organization(page_users, mail, password):
        page_users.login_users(page_users, mail, password)
        page_users.click(page_users.PageUsers.BUTTON_HEADER_ALLMS)
        page_users.expect_visible_element(page_users.PageAllMeasurements.TEXT_ALL_MEASUREMENTS)

    @staticmethod
    @pytest.mark.parametrize('mail', [mail_lan_doc])
    @pytest.mark.parametrize('password', [password_all])
    def test_header_meetings(page_users, mail, password):
        page_users.login_users(page_users, mail, password)
        page_users.click(page_users.PageUsers.BUTTON_HEADER_MEETING)
        page_users.expect_visible_element(page_users.PageMeetings.BUTTON_ADD_MEETING)

    @staticmethod
    @pytest.mark.parametrize('mail', mail_lan_doc)
    @pytest.mark.parametrize('password', [password_all])
    @pytest.mark.parametrize('locator', [Loc.PageUsers.BUTTON_HEADER_USERS,
                                         Loc.PageUsers.BUTTON_HEADER_ALLMS,
                                         Loc.PageUsers.BUTTON_HEADER_MEETING,
                                         Loc.PageUsers.BUTTON_ADD_USERS,
                                         Loc.PageUsers.BELL])
    def test_button_role_doc(page_users, mail, password, locator):
        page_users.login_users(page_users, mail, password)
        page_users.expect_visible_element(locator)

    @staticmethod
    @pytest.mark.parametrize('mail', mail_adm)
    @pytest.mark.parametrize('password', [password_all])
    @pytest.mark.parametrize('locator', [[Loc.PageUsers.BUTTON_HEADER_USERS,
                                         Loc.PageUsers.BUTTON_HEADER_ORGANIZATION,
                                         Loc.PageUsers.BUTTON_HEADER_SETTINGS,
                                         Loc.PageUsers.BUTTON_LOGS_AUDIT,
                                         Loc.PageUsers.BUTTON_LOAD_PATIENT,
                                         Loc.PageUsers.BUTTON_ADD_USERS]])
    def test_button_role_adm(page_users, mail, password, locator):
        page_users.login_users(page_users, mail, password)
        page_users.expect_visible_elements(locator)

    @staticmethod
    @pytest.mark.parametrize('mail', [mail_adm, mail_doc])
    @pytest.mark.parametrize('password', [password_all])
    def test_name_title_page(page_users, mail, password):
        page_users.login_users(page_users, mail, password)
        element = page_users.PageUsers.USERS_OR_PATIENTS
        page_users.wait_visible_elements(element)
        text = page_users.get_texts(element)
        if mail in mails_adm:
            assert "Пользователи" in text
        elif mail in mails_doc:
            assert "Пациенты" in text

    # @staticmethod
    # @pytest.mark.parametrize('mail', [mail for mail in cred])
    # @pytest.mark.parametrize('password', [password_all])
    # def test_quantity_users(page_users, mail, password):
    #     page_users.login_users(page_users, mail, password)
    #     head_quantity = page_users.get_text(page_users.PageUsers.QUANTITY_USERS_HEADER)
    #     top = re.split("(,)", head_quantity)
    #     top = top[0].strip('()')
    #     pag_quantity = page_users.get_text(page_users.PageUsers.QUANTITY_USERS_PAGINATION)
    #     bot = re.split("из ", pag_quantity)
    #     assert bot[1] in top 2

    class TestPagination:

        @staticmethod
        @pytest.mark.parametrize('mail', [mail for mail in mails_doc])
        @pytest.mark.parametrize('password', [password_all])
        @pytest.mark.parametrize('limit', [Loc.PageUsers.PAGINATION_20,
                                           Loc.PageUsers.PAGINATION_50,
                                           Loc.PageUsers.PAGINATION_100,
                                           Loc.PageUsers.PAGINATION_150])
        def test_quantity_user_limit(page_users, limit, mail, password):
            page_users.login_users(page_users, mail, password)
            page_users.click(limit)
            quantity_pagination = page_users.get_text(limit)
            quantity_users = page_users.get_quantity_elements(page_users.PageUsers.USERS_LIST)
            assert quantity_users == int(quantity_pagination)
            page_users.click(page_users.PageUsers.BUTTON_HEADER_ALLMS)

    # class TestChangePassword:
    #
    #     @staticmethod
    #     @pytest.mark.parametrize('mail', [mail_lan_doc])
    #     @pytest.mark.parametrize('password', [password_all])
    #     @pytest.mark.parametrize('new_password', [invalid_pass])
    #     def test_valid_change_password(page_users, mail, password, new_password):
    #         create_user_get_id = page_users.api_create_doctor(mail, password_all)
    #         page_users.login_users(page_users, mail, password)
    #         page_users.click(page_users.PageUsers.NAME_PROFILE)
    #         page_users.click(page_users.PageUsers.BUTTON_CHANGE_PASSWORD)
    #         page_users.change_password(page_users, password, new_password)
    #         page_users.click(page_users.PageUsers.BUTTON_SAVE_NEW_PASS)
    #         page_users.wait_for_element_visible(page_users.GeneralLocators.NOTIFICATION_ALL)
    #         page_users.api_delete_user(create_user_get_id)
    #
    #     @staticmethod
    #     @pytest.mark.parametrize('mail', [mail_lan_doc])
    #     @pytest.mark.parametrize('password', [password_all])
    #     @pytest.mark.parametrize('new_password', [invalid_pass])
    #     def test_invalid_without_current_password(page_users, mail, password, new_password):
    #         create_user_get_id = page_users.api_create_doctor(mail, password_all)
    #         page_users.login_users(page_users, mail, password)
    #         page_users.click(page_users.PageUsers.NAME_PROFILE)
    #         page_users.click(page_users.PageUsers.BUTTON_CHANGE_PASSWORD)
    #         page_users.fill_text(page_users.PageUsers.INPUT_NEW_PASS, invalid_pass)
    #         page_users.fill_text(page_users.PageUsers.INPUT_NEW2_PASS, invalid_pass)
    #         page_users.click(page_users.PageUsers.BUTTON_SAVE_NEW_PASS)
    #         page_users.wait_for_element_visible(page_users.GeneralLocators.NOTIFICATION_ALL)
    #         page_users.api_delete_user(create_user_get_id)
    #
    #     @staticmethod
    #     @pytest.mark.parametrize('mail', [mail_lan_doc])
    #     @pytest.mark.parametrize('password', [password_all])
    #     @pytest.mark.parametrize('new_password', [invalid_pass])
    #     def test_invalid_without_re_password(page_users, mail, password, new_password):
    #         create_user_get_id = page_users.api_create_doctor(mail, password_all)
    #         page_users.login_users(page_users, mail, password)
    #         page_users.click(page_users.PageUsers.NAME_PROFILE)
    #         page_users.click(page_users.PageUsers.BUTTON_CHANGE_PASSWORD)
    #         page_users.fill_text(page_users.PageUsers.INPUT_CURRENT_PASS, password_all)
    #         page_users.fill_text(page_users.PageUsers.INPUT_NEW_PASS, invalid_pass)
    #         page_users.click(page_users.PageUsers.BUTTON_SAVE_NEW_PASS)
    #         page_users.wait_for_element_visible(page_users.GeneralLocators.NOTIFICATION_ALL)
    #         page_users.api_delete_user(create_user_get_id)
    #
    #
    #     @staticmethod
    #     @pytest.mark.parametrize('mail', [mail_doc])
    #     @pytest.mark.parametrize('password', [password_all])
    #     @pytest.mark.parametrize('body_input', [[Loc.PageUsers.INPUT_CURRENT_PASS,
    #                                              Loc.PageUsers.INPUT_NEW_PASS,
    #                                              Loc.PageUsers.INPUT_NEW2_PASS]])
    #     @pytest.mark.parametrize('placeholder_input', [[Loc.PageUsers.PLACEHOLDER_CURRENT_PASS,
    #                                                     Loc.PageUsers.PLACEHOLDER_NEW_PASS,
    #                                                     Loc.PageUsers.PLACEHOLDER_NEW2_PASS]])
    #     def test_color_input_change_password(page_users, mail, password, body_input, placeholder_input):
    #         page_users.login_users(page_users, mail, password)
    #         page_users.click(page_users.PageUsers.NAME_PROFILE)
    #         page_users.click(page_users.PageUsers.BUTTON_CHANGE_PASSWORD)
    #         page_users.click(page_users.PageUsers.BUTTON_SAVE_NEW_PASS)
    #         page_users.expect_invalid_input_color(placeholder_input, body_input)
    #         page_users.wait_for_element_visible(page_users.GeneralLocators.NOTIFICATION_ALL)

    # class TestChangeProfile:
    #
    #     @staticmethod
    #     @pytest.mark.parametrize('mail', [mail_lan_doc])
    #     @pytest.mark.parametrize('password', [password_all])
    #     @pytest.mark.parametrize('body_input', [[Loc.PageUsers.INPUT_CHANGE_F,
    #                                              Loc.PageUsers.INPUT_CHANGE_I,
    #                                              Loc.PageUsers.INPUT_CHANGE_MAIL,
    #                                              Loc.PageUsers.INPUT_CHANGE_PHONE]])
    #     @pytest.mark.parametrize('placeholder_input', [[Loc.PageUsers.PLACEHOLDER_CHANGE_F,
    #                                                     Loc.PageUsers.PLACEHOLDER_CHANGE_I,
    #                                                     Loc.PageUsers.PLACEHOLDER_CHANGE_MAIL,
    #                                                     Loc.PageUsers.PLACEHOLDER_CHANGE_PHONE]])
    #     def test_empty_input_change_profile(page_users, mail, password, body_input, placeholder_input):
    #         page_users.login_users(page_users, mail, password)
    #         page_users.click(page_users.PageUsers.NAME_PROFILE)
    #         page_users.click(page_users.PageUsers.BUTTON_CHANGE_PROFILE)
    #         page_users.clear_inputs(body_input)
    #         page_users.click(page_users.PageUsers.BUTTON_SAVE_PROFILE)
    #         text_notif = page_users.get_texts(page_users.GeneralLocators.NOTIFICATION_ALL)
    #         assert text_notif == "Ошибка при изменении пользователя"
    #         page_users.wait_until_visible_elements(page_users.GeneralLocators.NOTIFICATION_ALL)
    #
    #     @staticmethod
    #     @pytest.mark.parametrize('mail', [mail_lan_doc])
    #     @pytest.mark.parametrize('password', [password_all])
    #     @pytest.mark.parametrize('body_input', [[Loc.PageUsers.INPUT_CHANGE_F,
    #                                              Loc.PageUsers.INPUT_CHANGE_I,
    #                                              Loc.PageUsers.INPUT_CHANGE_MAIL,
    #                                              Loc.PageUsers.INPUT_CHANGE_PHONE]])
    #     @pytest.mark.parametrize('placeholder_input', [[Loc.PageUsers.PLACEHOLDER_CHANGE_F,
    #                                                     Loc.PageUsers.PLACEHOLDER_CHANGE_I,
    #                                                     Loc.PageUsers.PLACEHOLDER_CHANGE_MAIL,
    #                                                     Loc.PageUsers.PLACEHOLDER_CHANGE_PHONE]])
    #     def test_color_required_field_change_profile(page_users, mail, password, body_input, placeholder_input):
    #         page_users.login_users(page_users, mail, password)
    #         page_users.click(page_users.PageUsers.NAME_PROFILE)
    #         page_users.click(page_users.PageUsers.BUTTON_CHANGE_PROFILE)
    #         page_users.clear_inputs(body_input)
    #         page_users.click(page_users.PageUsers.BUTTON_SAVE_PROFILE)
    #         page_users.expect_invalid_input_color(placeholder_input, body_input)
    #         page_users.wait_until_visible_elements(page_users.GeneralLocators.NOTIFICATION_ALL)
    #
    #     @staticmethod
    #     @pytest.mark.parametrize('mail', [mail_lan_doc])
    #     @pytest.mark.parametrize('password', [password_all])
    #     @pytest.mark.parametrize('button_close', [Loc.PageUsers.BUTTON_CLOSE_CHANGE_PROFILE,
    #                                               Loc.PageUsers.BUTTON_X_CHANGE_PROFILE])
    #     def test_close_change_profile(page_users, mail, password, button_close):
    #         page_users.login_users(page_users, mail, password)
    #         page_users.click(page_users.PageUsers.NAME_PROFILE)
    #         page_users.click(page_users.PageUsers.BUTTON_CHANGE_PROFILE)
    #         page_users.click(button_close)
    #         page_users.expect_not_visible_elements(page_users.PageUsers.WINDOW_CHANGE_PROFILE)

    # class TestAddUsers:

        # @staticmethod
        # @pytest.mark.parametrize('mail', [random_mail()])
        # @pytest.mark.parametrize('org_id', [100, 101, 102, 103])
        # @pytest.mark.parametrize('password', [password_all])
        # def test_valid_add_doctor_required_field(page_users, mail, password, org_id):
        #     access_token = page_users.api_get_access_token_adm(org_id)
        #     user_id = page_users.api_create_doctor(mail, password, access_token, org_id)
        #     page_users.login_users(page_users, mail, password)
        #     page_users.click(page_users.PageUsers.BUTTON_ADD_USERS)
        #     page_users.fill_text(page_users.PageUsers.INPUT_ADD_USER_F, random_fio('F'))
        #     page_users.fill_text(page_users.PageUsers.INPUT_ADD_USER_I, random_fio('I'))
        #     page_users.fill_text(page_users.PageUsers.INPUT_ADD_USER_DATA, random_data())
        #     page_users.click(page_users.PageUsers.INPUT_ADD_USER_ORG)
        #     page_users.open_dropdown_organization()
        #     page_users.click(page_users.PageUsers.ORG_TELCENT_AMBULANCE_CRB1_FAP1)
        #     page_users.click(page_users.PageUsers.BUTTON_ADD_USER_IN_WINDOW)
        #     notification = page_users.GeneralLocators.NOTIFICATION_ALL
        #     page_users.wait_visible_elements(notification)
        #     assert page_users.get_texts(notification) == "Пользователь успешно добавленДиагнозы успешно изменены"
        #     page_users.expect_visible_elements(page_users.PageUsers.DIV_SUCCESSFULLY_CREATED)
        #     page_users.wait_until_visible_elements(notification)
        #     page_users.api_delete_user(user_id, access_token)

        # @staticmethod
        # @pytest.mark.parametrize('mail', [mail_doc])
        # @pytest.mark.parametrize('password', [password_all])
        # def test_valid_add_user_all_field(page_users, mail, password):
        #     page_users.login_users(page_users, mail, password)
        #     page_users.click(page_users.PageUsers.BUTTON_ADD_USERS)
        #     page_users.fill_text(page_users.PageUsers.INPUT_ADD_USER_F, random_fio('F'))
        #     page_users.fill_text(page_users.PageUsers.INPUT_ADD_USER_I, random_fio('I'))
        #     page_users.fill_text(page_users.PageUsers.INPUT_ADD_USER_O, random_fio('O'))
        #     page_users.fill_text(page_users.PageUsers.INPUT_ADD_USER_DATA, random_data())
        #     page_users.fill_text(page_users.PageUsers.INPUT_ADD_USER_HEIGHT, random_height_weight())
        #     page_users.fill_text(page_users.PageUsers.INPUT_ADD_USER_WEIGHT, random_height_weight())
        #     page_users.fill_text(page_users.PageUsers.INPUT_ADD_USER_MAIL, random_mail())
        #     page_users.fill_text(page_users.PageUsers.INPUT_ADD_USER_PHONE, random_phone())
        #     page_users.click(page_users.PageUsers.INPUT_ADD_USER_ORG)
        #     page_users.open_dropdown_organization()
        #     page_users.click(page_users.PageUsers.ORG_TELCENT_AMBULANCE_CRB1_FAP1)
        #     page_users.click(page_users.PageUsers.INPUT_ADD_USER_DIAGNOSES)
        #     page_users.click(page_users.PageUsers.INPUT_ADD_USER_DIAGNOSES_CHOOSE_ALL)
        #     page_users.click(page_users.PageUsers.BUTTON_ADD_USER_IN_WINDOW)
        #     notification = page_users.GeneralLocators.NOTIFICATION_ALL
        #     page_users.wait_visible_elements(notification)
        #     assert page_users.get_texts(notification) == "Пользователь успешно добавленДиагнозы успешно изменены"
        #     page_users.expect_visible_elements(page_users.PageUsers.DIV_SUCCESSFULLY_CREATED)
        #     page_users.wait_until_visible_elements(notification)

#         @staticmethod
#         @pytest.mark.parametrize('mail', [mail_lan_doc])
#         @pytest.mark.parametrize('password', [password_all])
#         @pytest.mark.parametrize('body_input', [[Loc.PageUsers.INPUT_ADD_USER_F,
#                                                 Loc.PageUsers.INPUT_ADD_USER_I,
#                                                 Loc.PageUsers.INPUT_ADD_USER_DATA,
#                                                 Loc.PageUsers.INPUT_ADD_USER_ORG]])
#         @pytest.mark.parametrize('placeholder_input', [[Loc.PageUsers.PLACEHOLDER_ADD_USER_F,
#                                                         Loc.PageUsers.PLACEHOLDER_ADD_USER_I,
#                                                         Loc.PageUsers.PLACEHOLDER_ADD_USER_DATA,
#                                                         Loc.PageUsers.PLACEHOLDER_ADD_USER_ORG]])
#         def test_empty_input_field_add_user(page_users, mail, password, body_input, placeholder_input):
#             page_users.login_users(page_users, mail, password)
#             page_users.click(page_users.PageUsers.BUTTON_ADD_USERS)
#             page_users.click(page_users.PageUsers.BUTTON_ADD_USER_IN_WINDOW)
#             page_users.expect_invalid_input_color(placeholder_input, body_input)
#             notification = page_users.GeneralLocators.NOTIFICATION_ALL
#             text_notification = page_users.get_texts(notification)
#             assert text_notification == "Заполните все обязательные поля"
#             page_users.wait_until_visible_elements(notification)
#
#
# class TestFilter:
#
#         @staticmethod
#         @pytest.mark.parametrize('mail', [mail_lan_doc, mail_lan_adm])
#         @pytest.mark.parametrize('password', [password_all])
#         def test_boxs_input_filter(page_users, mail, password):
#             page_users.login_users(page_users, mail, password)
#             page_users.dropdown_filter()
#             page_users.click_on_elements(page_users.PageUsers.FILTER_INPUT_BOXS)
#
#         @staticmethod
#         @pytest.mark.parametrize('mail', [mail_lan_doc, mail_lan_adm])
#         @pytest.mark.parametrize('password', [password_all])
#         def test_boxs_dropdown_filter(page_users, mail, password):
#             page_users.login_users(page_users, mail, password)
#             page_users.dropdown_filter()
#             page_users.click(page_users.PageUsers.FILTER_DROPDOWN_GENDER)
#             page_users.wait_visible_elements(page_users.PageUsers.FILTER_CONTAINER_GENDER)
#             page_users.click(page_users.PageUsers.FILTER_DROPDOWN_ORG)
#             page_users.wait_visible_elements(page_users.PageUsers.FILTER_CONTAINER_ORG_ROLE)
#             if mail in mail_lan_adm:
#                 page_users.click(page_users.PageUsers.FILTER_DROPDOWN_ROLE)
#                 page_users.wait_visible_elements(page_users.PageUsers.FILTER_CONTAINER_ORG_ROLE)
#
