from PageLocators.locators import LocatorsGeneral
import pytest
from tests.config import *



@pytest.mark.parametrize('url', list_url_test)
class TestGeneralElements:
    @pytest.mark.parametrize('elements', [[LocatorsGeneral.LOGO_SAMGMU,
                                           LocatorsGeneral.YEAR_BOT,
                                           LocatorsGeneral.HELP_LINK,
                                           LocatorsGeneral.SUPPORTS_LINK]])
    def test_general_elements(self, page_general, elements, url):
        page_general.open(url)
        if url is url_users_test:
            page_general.login_users("doc@tele.com", "12345678")
        page_general.expect_visible_elements(elements)

    @pytest.mark.parametrize('link_element', [LocatorsGeneral.HELP_LINK,
                                              LocatorsGeneral.SUPPORTS_LINK])
    def test_open_link(self, page_general, link_element, url):
        if url is not url_users_test:
            page_general.open(url)
            page_general.click(link_element)
            if link_element is LocatorsGeneral.HELP_LINK:
                assert page_general.get_uri() == url_help_test
            elif link_element is LocatorsGeneral.SUPPORTS_LINK:
                assert page_general.get_uri() == url_support_test

