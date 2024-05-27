from tests.config import *
import time
import pytest
import json
from playwright.sync_api import Route
from PageLocators.locators import LocatorsPage as Loc


@pytest.mark.parametrize('mail, name', [(mail, name) for mail, name in cred.items()])
@pytest.mark.parametrize('password', [password_all])
def test_auth(page_auth, mail, password, name):
    page_auth.login_users(page_auth, mail, password)
    page_auth.expect_visible_element(page_auth.NAME_PROFILE)
    page_auth.screenshot(dop=mail)


@pytest.mark.parametrize('mail', ["testdoc@doc.doc", "doc@doc.com", "testdoc@doc.com", "d.s.ivanov1@samsmu.ru"])
@pytest.mark.parametrize('password', [password_all])
@pytest.mark.parametrize('locator', [Loc.BUTTON_HEADER_USERS,
                                     Loc.BUTTON_HEADER_ALLMS,
                                     Loc.BUTTON_HEADER_MEETING,
                                     Loc.BUTTON_ADD_PATIENT])
def test_button_role_doc(page_auth, mail, password, locator):
    page_auth.login_users(page_auth, mail, password)
    page_auth.expect_visible_element(locator)


@pytest.mark.parametrize('mail', ["adm@adm.com", "spadm@adm.adm", "testadm@adm.adm"])
@pytest.mark.parametrize('password', [password_all])
@pytest.mark.parametrize('locator', [Loc.BUTTON_HEADER_USERS,
                                     Loc.BUTTON_HEADER_ORGANIZATION,
                                     Loc.BUTTON_HEADER_SETTINGS,
                                     Loc.BUTTON_LOGS_AUDIT,
                                     Loc.BUTTON_LOAD_PATIENT,
                                     Loc.BUTTON_ADD_USERS])
def test_button_role_adm(page_auth, mail, password, locator):
    page_auth.login_users(page_auth, mail, password)
    page_auth.login_users(page_auth, mail, password)
    page_auth.expect_visible_element(locator)


