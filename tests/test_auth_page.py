import pytest


class TestAuth:

    @pytest.mark.parametrize('mail', ['doc@tele.com',
                                      'doc@amb.com',
                                      'doc@crb.com'])
    def test_valid_log_in(self, auth_page, mail):
        auth_page.test_valid_log_in(mail)

    def test_log_in_admin_tele(self, auth_page):
        name_profile = auth_page.input_admin_tele()
        auth_page.input_valid_password()
        auth_page.click_log_in()
        auth_page.expect_valid_auth(name_profile)

    def test_log_in_admin_amb(self, auth_page):
        name_profile = auth_page.input_admin_amb()
        auth_page.input_valid_password()
        auth_page.click_log_in()
        auth_page.expect_valid_auth(name_profile)

    def test_log_in_admin_crb(self, auth_page):
        name_profile = auth_page.input_admin_crb()
        auth_page.input_valid_password()
        auth_page.click_log_in()
        auth_page.expect_valid_auth(name_profile)

    def test_log_in_doctor_tele(self, auth_page):
        name_profile = auth_page.input_doctor_tele()
        auth_page.input_valid_password()
        auth_page.click_log_in()
        auth_page.expect_valid_auth(name_profile)

    def test_log_in_doctor_amb(self, auth_page):
        name_profile = auth_page.input_doctor_amb()
        auth_page.input_valid_password()
        auth_page.click_log_in()
        auth_page.expect_valid_auth(name_profile)

    def test_log_in_doctor_crb(self, auth_page):
        name_profile = auth_page.input_doctor_crb()
        auth_page.input_valid_password()
        auth_page.click_log_in()
        auth_page.expect_valid_auth(name_profile)

    def test_invalid_password(self, auth_page):
        auth_page.input_doctor_crb()
        auth_page.input_invalid_password()
        auth_page.click_log_in()
        auth_page.expect_error_invalid_password()

    def test_invalid_mail(self, auth_page):
        auth_page.input_invalid_mail()
        auth_page.input_invalid_password()
        auth_page.click_log_in()
        auth_page.expect_error_invalid_mail()

    def test_visible_main_elements(self, auth_page):
        auth_page.expect_visible_all_elements()

    def test_reducing_placeholder_on_click(self, auth_page):
        auth_page.expect_reducing_placeholder_mail()
        auth_page.expect_reducing_placeholder_password()

    def test_hide_show_password(self, auth_page):
        auth_page.expect_input_password_is_password()
        auth_page.click_eye_password()
        auth_page.expect_input_password_is_text()
        auth_page.click_eye_password()
        auth_page.expect_input_password_is_password()

    def test_red_color_input_mail(self, auth_page):
        auth_page.click_log_in()
        auth_page.expect_color_input_mail_is_red()

    def test_red_color_input_password(self, auth_page):
        auth_page.click_log_in()
        auth_page.expect_color_input_password_is_red()


class TestForgotPassword:

    def test_valid_forgot_password(self, auth_page):
        auth_page.click_on_forgot_password()
        mail = auth_page.input_mail_for_forgot_password()
        auth_page.click_on_reset_password()
        auth_page.expect_notification_valid_reset(mail)

    def test_forgot_password_empty_mail(self, auth_page):
        auth_page.click_on_forgot_password()
        auth_page.click_on_reset_password()
        auth_page.expect_notification_invalid_reset()

    def test_forgot_password_invalid_mail(self, auth_page):
        auth_page.click_on_forgot_password()
        mail = auth_page.input_invalid_mail()
        auth_page.click_on_reset_password()
        auth_page.expect_notification_invalid_reset(mail)

    def test_cancel_forgot_password(self, auth_page):
        auth_page.click_on_forgot_password()
        auth_page.click_cancel_forgot_password()

    def test_color_input_mail_forgot(self, auth_page):
        auth_page.click_on_forgot_password()
        auth_page.click_on_reset_password()
        auth_page.expect_color_input_mail_is_red()
