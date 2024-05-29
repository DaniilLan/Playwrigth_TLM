from tests.config import *
import time
import pytest
import json
from playwright.sync_api import Route
from PageLocators.locators import Locators as Loc
import re


def test(page):
    page.login_users(page, 'doc@doc.com', '12345678')
    page.click('//*[@id="rootTelemedHub"]/div[2]/header/div/div[3]/div/div[3]/div/div/div[1]/div')
    page.click('//html/body/div[2]/div/div[2]')
    page.click('//html/body/div[2]/div/div[2]/form/div[7]/button[2]')
    page.wait_for_element_visible('//*[@id="rootTelemedHub"]/div[1]/div')
    page.click('//html/body/div[2]/div/div[1]/div')



# class TestPageLogin:
#     @staticmethod
#     @pytest.mark.parametrize('mail, name', [(mail, name) for mail, name in cred.items()])
#     @pytest.mark.parametrize('password', [password_all])
#     def test_auth(page, mail, password, name):
#         page.login_users(page, mail, password)
#         page.expect_visible_element(page.PageUsers.NAME_PROFILE)
#         page.screenshot(dop=mail)
#
#
# class TestPageUsers:
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
