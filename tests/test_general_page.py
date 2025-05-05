from locators.base_locators import LocatorsBase

import pytest


@pytest.mark.parametrize('url', list_url_test)
class TestGeneralElements:
    @pytest.mark.parametrize('elements', [[LocatorsBase.LOGO_SAMGMU,
                                           LocatorsBase.YEAR_BOT,
                                           LocatorsBase.HELP_LINK,
                                           LocatorsBase.SUPPORTS_LINK]])
    def test_general_elements(self, page_auth, elements, url):
        page_auth.open(url)
        if url is url_users_test:
            page_auth.login_users("doc@tele.com", "12345678")
        page_auth.expect_visible_elements(elements)

    @pytest.mark.parametrize('link_element', [LocatorsBase.HELP_LINK,
                                              LocatorsBase.SUPPORTS_LINK])
    def test_open_link(self, page_auth, link_element, url):
        if url is not url_users_test:
            page_auth.open(url)
            page_auth.click(link_element)
            if link_element is LocatorsBase.HELP_LINK:
                assert page_auth.get_uri() == url_help_test
            elif link_element is LocatorsBase.SUPPORTS_LINK:
                assert page_auth.get_uri() == url_support_test

