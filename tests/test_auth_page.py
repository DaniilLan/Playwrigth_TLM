import time
import pytest


class TestAuth:

    # def test_create_user(self, auth_page, test_user):
    #     time.sleep(10)

    # def test_log_in_admin_tele(self, auth_page):
    #     name_profile = auth_page.input_admin_tele()
    #     auth_page.input_valid_password()
    #     auth_page.click_log_in()
    #     auth_page.expect_valid_auth(name_profile)
    #
    # def test_log_in_admin_amb(self, auth_page):
    #     name_profile = auth_page.input_admin_amb()
    #     auth_page.input_valid_password()
    #     auth_page.click_log_in()
    #     auth_page.expect_valid_auth(name_profile)
    #
    # def test_log_in_admin_crb(self, auth_page):
    #     name_profile = auth_page.input_admin_crb()
    #     auth_page.input_valid_password()
    #     auth_page.click_log_in()
    #     auth_page.expect_valid_auth(name_profile)
    #
    # def test_log_in_doctor_tele(self, auth_page):
    #     name_profile = auth_page.input_doctor_tele()
    #     auth_page.input_valid_password()
    #     auth_page.click_log_in()
    #     auth_page.expect_valid_auth(name_profile)
    #
    # def test_log_in_doctor_amb(self, auth_page):
    #     name_profile = auth_page.input_doctor_amb()
    #     auth_page.input_valid_password()
    #     auth_page.click_log_in()
    #     auth_page.expect_valid_auth(name_profile)
    #
    # def test_log_in_doctor_crb(self, auth_page):
    #     name_profile = auth_page.input_doctor_crb()
    #     auth_page.input_valid_password()
    #     auth_page.click_log_in()
    #     auth_page.expect_valid_auth(name_profile)
    #
    # def test_invalid_password(self, auth_page):
    #     auth_page.input_doctor_crb()
    #     auth_page.input_invalid_password()
    #     auth_page.click_log_in()
    #     auth_page.expect_error_invalid_password()
    #
    # def test_invalid_mail(self, auth_page):
    #     auth_page.input_invalid_mail()
    #     auth_page.input_invalid_password()
    #     auth_page.click_log_in()
    #     auth_page.expect_error_invalid_mail()
    #
    # def test_visible_main_elements(self, auth_page):
    #     auth_page.expect_visible_all_elements()
    #
    # def test_reducing_placeholder_on_click(self, auth_page):
    #     auth_page.expect_reducing_placeholder_mail()
    #     auth_page.expect_reducing_placeholder_password()
    #
    # def test_hide_show_password(self, auth_page):
    #     auth_page.expect_input_password_is_password()
    #     auth_page.click_eye_password()
    #     auth_page.expect_input_password_is_text()
    #     auth_page.click_eye_password()
    #     auth_page.expect_input_password_is_password()
    #
    # def test_red_color_input_mail(self, auth_page):
    #     auth_page.click_log_in()
    #     auth_page.expect_color_input_mail_is_red()
    #
    # def test_red_color_input_password(self, auth_page):
    #     auth_page.click_log_in()
    #     auth_page.expect_color_input_password_is_red()

    def test_valid_forgot_password(self, auth_page):
        auth_page.click_on_link_forgot_password()
        mail = auth_page.input_mail_for_forgot_password()
        auth_page.click_on_reset_password()
        auth_page.expect_notification_valid_reset(mail)

    def test_forgot_password_empty_mail(self, auth_page):
        auth_page.click_on_link_forgot_password()
        auth_page.click_on_reset_password()
        auth_page.expect_notification_invalid_reset()

    def test_forgot_password_invalid_mail(self, auth_page):
        auth_page.click_on_link_forgot_password()
        mail = auth_page.input_invalid_mail()
        auth_page.click_on_reset_password()
        auth_page.expect_notification_invalid_reset(mail)

    def test_cancel_forgot_password(self, auth_page):
        auth_page.click_on_link_forgot_password()
        auth_page.click_cancel_forgot_password()

    def test_red_color_input_mail_forgot(self, auth_page):
        auth_page.click_on_link_forgot_password()
        auth_page.click_on_reset_password()
        auth_page.expect_color_input_mail_is_red()

    def test_disappearing_button_reset(self, auth_page):
        auth_page.click_on_link_forgot_password()
        auth_page.click_on_reset_password()
        auth_page.expect_color_input_mail_is_red()
    #
    # def test_pop_up_hovering_input_field(self, auth_page):
    #     auth_page.click_log_in()
    #     auth_page.hovering_on_input_field_mail()
    #     auth_page.expect_visible_pop_up_required_email()
    #     auth_page.hovering_on_input_field_password()
    #     auth_page.expect_visible_pop_up_required_password()
    #
    # def test_go_tu_page_halp(self, auth_page):
    #     auth_page.click_on_link_help()
    #     auth_page.expect_valid_go_to_help_page()
    #
    # def test_go_tu_page_support(self, auth_page):
    #     auth_page.click_on_link_support()
    #     auth_page.expect_valid_go_to_support_page()
    #
    # def test_pop_up_hovering_input_field_forgot_password(self, auth_page):
    #     auth_page.click_on_link_forgot_password()
    #     auth_page.click_on_reset_password()
    #     auth_page.hovering_on_input_field_mail()
    #     auth_page.expect_visible_pop_up_required_email()
    #
    # def test_refresh_page_using_logo(self, auth_page):
    #     auth_page.click_on_logo()
    #     auth_page.expect_url_is_auth()