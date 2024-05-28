from tests.config import *
import time
import pytest
import json
from playwright.sync_api import Route
from PageLocators.locators import LocatorsPage as Loc
import re


# @pytest.mark.parametrize('mail, name', [(mail, name) for mail, name in cred.items()])
# @pytest.mark.parametrize('password', [password_all])
# def test_auth(page_auth, mail, password, name):
#     page_auth.login_users(page_auth, mail, password)
#     page_auth.expect_visible_element(page_auth.NAME_PROFILE)
#     page_auth.screenshot(dop=mail)
#
#
# @pytest.mark.parametrize('mail', ["testdoc@doc.doc", "doc@doc.com", "testdoc@doc.com", "d.s.ivanov1@samsmu.ru"])
# @pytest.mark.parametrize('password', [password_all])
# @pytest.mark.parametrize('locator', [Loc.BUTTON_HEADER_USERS,
#                                      Loc.BUTTON_HEADER_ALLMS,
#                                      Loc.BUTTON_HEADER_MEETING,
#                                      Loc.BUTTON_ADD_PATIENT])
# def test_button_role_doc(page_auth, mail, password, locator):
#     page_auth.login_users(page_auth, mail, password)
#     page_auth.expect_visible_element(locator)
#
#
# @pytest.mark.parametrize('mail', ["adm@adm.com", "spadm@adm.adm", "testadm@adm.adm"])
# @pytest.mark.parametrize('password', [password_all])
# @pytest.mark.parametrize('locator', [Loc.BUTTON_HEADER_USERS,
#                                      Loc.BUTTON_HEADER_ORGANIZATION,
#                                      Loc.BUTTON_HEADER_SETTINGS,
#                                      Loc.BUTTON_LOGS_AUDIT,
#                                      Loc.BUTTON_LOAD_PATIENT,
#                                      Loc.BUTTON_ADD_USERS])
# def test_button_role_adm(page_auth, mail, password, locator):
#     page_auth.login_users(page_auth, mail, password)
#     page_auth.expect_visible_element(locator)
#
#
# @pytest.mark.parametrize('mail', [mail for mail in cred])
# @pytest.mark.parametrize('password', [password_all])
# def test_text_(page_auth, mail, password):
#     page_auth.login_users(page_auth, mail, password)
#     if mail in ["adm@adm.com", "spadm@adm.adm", "testadm@adm.adm"]:
#         page_auth.wait_visible_all()
#         assert "Пользователи" in page_auth.get_text(page_auth.USERS_OR_PATIENTS)
#     elif mail in ["testdoc@doc.doc", "doc@doc.com", "testdoc@doc.com", "d.s.ivanov1@samsmu.ru"]:
#         page_auth.wait_visible_all()
#         assert "Пациенты" in page_auth.get_text(page_auth.USERS_OR_PATIENTS)
#
#
# @pytest.mark.parametrize('mail', [mail for mail in cred])
# @pytest.mark.parametrize('password', [password_all])
# def test_quantity_users(page_auth, mail, password):
#     page_auth.login_users(page_auth, mail, password)
#     head_quantity = page_auth.get_text(page_auth.QUANTITY_USERS_HEADER)
#     top = re.split("(,)", head_quantity)
#     pag_quantity = page_auth.get_text(page_auth.QUANTITY_USERS_PAGINATION)
#     bot = re.split("(из )", head_quantity)
#     assert top == bot

@pytest.mark.parametrize('mail', [mail for mail in cred])
@pytest.mark.parametrize('password', [password_all])
def test_boxs_dropdown_filter(page_auth, mail, password):
    page_auth.login_users(page_auth, mail, password)
    page_auth.click(page_auth.DROPDOWN_FILTER)
    page_auth.click_on_elements(page_auth.FILTER_INPUT_BOXS)


