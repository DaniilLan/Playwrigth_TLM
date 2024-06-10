from tests.config import *
import time
import pytest
import json
from playwright.sync_api import Route
from PageLocators.locators import Locators as Loc
import re


@pytest.mark.parametrize('url', list_url_test)
class TestGeneralElements:
    @staticmethod
    @pytest.mark.parametrize('elements', [[Loc.GeneralLocators.LOGO_SAMGMU,
                                           Loc.GeneralLocators.YEAR_BOT,
                                           Loc.GeneralLocators.HELP_LINK,
                                           Loc.GeneralLocators.SUPPORTS_LINK]])
    def test_general_elements(page_general, elements, url):
        page_general.open(url)
        if url is url_users_test:
            page_general.login_users(page_general, "adm@adm.com", "12345678")
        page_general.expect_visible_elements(elements)

    @staticmethod
    @pytest.mark.parametrize('link_element', [Loc.GeneralLocators.HELP_LINK,
                                              Loc.GeneralLocators.SUPPORTS_LINK])
    def test_open_link(page_general, link_element, url):
        if url is not url_users_test:
            page_general.open(url)
            page_general.click(link_element)
            if link_element is Loc.GeneralLocators.HELP_LINK:
                assert page_general.get_url() == url_help_test
            elif link_element is Loc.GeneralLocators.SUPPORTS_LINK:
                assert page_general.get_url() == url_support_test

