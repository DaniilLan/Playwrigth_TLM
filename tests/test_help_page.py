import allure
import pytest


class TestHelp:

    def test_open_panel_terms(self, help_page):
        help_page.click_on_topic_terms()
        help_page.expect_visible_panel_terms()

    def test_open_panel_registration(self, help_page):
        help_page.click_on_topic_registration()
        help_page.expect_visible_panel_registration()

    def test_open_panel_authorization(self, help_page):
        help_page.click_on_topic_authorization()
        help_page.expect_visible_panel_authorization()

    def test_open_panel_password_recover(self, help_page):
        help_page.click_on_topic_password_recover()
        help_page.expect_visible_panel_password_recover()

    def test_open_panel_profile_setup(self, help_page):
        help_page.click_on_topic_profile_setup()
        help_page.expect_visible_panel_profile_setup()

    def test_open_panel_help_for_admin(self, help_page):
        help_page.click_on_topic_help_for_admin()
        help_page.expect_visible_panel_help_for_admin()

    def test_open_panel_help_for_doctor(self, help_page):
        help_page.click_on_topic_help_for_doctor()
        help_page.expect_visible_panel_help_for_doctor()

    def test_open_user_manual(self, help_page):
        help_page.click_on_user_manual()

    def test_go_to_auth(self, help_page):
        help_page.click_on_button_auth()
        help_page.expect_valid_go_to_auth_page()

    def test_go_to_page_halp(self, help_page):
        help_page.click_on_link_help()
        help_page.expect_valid_click_on_link_help()

    def test_go_to_page_support(self, help_page):
        help_page.click_on_link_support()
        help_page.expect_valid_go_to_support_page()

    def test_go_to_auth_page_through_logo(self, help_page):
        help_page.click_on_logo()
        help_page.expect_url_is_auth()
