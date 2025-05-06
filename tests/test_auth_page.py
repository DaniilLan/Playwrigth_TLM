import pytest

class TestPageAuth:

    def test_log_in_admin_tele(self, page_auth):
        name_profile = page_auth.input_admin_tele()
        page_auth.input_valid_password()
        page_auth.click_log_in()
        page_auth.expect_valid_auth(name_profile)

    def test_log_in_admin_amb(self, page_auth):
        name_profile = page_auth.input_admin_amb()
        page_auth.input_valid_password()
        page_auth.click_log_in()
        page_auth.expect_valid_auth(name_profile)

    def test_log_in_admin_crb(self, page_auth):
        name_profile = page_auth.input_admin_crb()
        page_auth.input_valid_password()
        page_auth.click_log_in()
        page_auth.expect_valid_auth(name_profile)

    def test_log_in_doctor_tele(self, page_auth):
        name_profile = page_auth.input_doctor_tele()
        page_auth.input_valid_password()
        page_auth.click_log_in()
        page_auth.expect_valid_auth(name_profile)

    def test_log_in_doctor_amb(self, page_auth):
        name_profile = page_auth.input_doctor_amb()
        page_auth.input_valid_password()
        page_auth.click_log_in()
        page_auth.expect_valid_auth(name_profile)

    def test_log_in_doctor_crb(self, page_auth):
        name_profile = page_auth.input_doctor_crb()
        page_auth.input_valid_password()
        page_auth.click_log_in()
        page_auth.expect_valid_auth(name_profile)

    def test_invalid_password(self, page_auth):
        page_auth.input_doctor_crb()
        page_auth.input_invalid_password()
        page_auth.click_log_in()
        page_auth.expect_error_invalid_password()

    def test_invalid_mail(self, page_auth):
        page_auth.input_invalid_mail()
        page_auth.input_invalid_password()
        page_auth.click_log_in()
        page_auth.expect_error_invalid_mail()

    def test_visible_main_elements(self, page_auth):
        page_auth.expect_visible_all_elements()

    def test_reducing_placeholder_on_click(self, page_auth):
        page_auth.expect_reducing_placeholder_mail()
        page_auth.expect_reducing_placeholder_password()

    def test_hide_show_password(self, page_auth):
        page_auth.expect_input_password_is_password()
        page_auth.click_eye_password()
        page_auth.expect_input_password_is_text()
        page_auth.click_eye_password()
        page_auth.expect_input_password_is_password()

    def test_red_color_input_mail(self, page_auth):
        page_auth.click_log_in()
        page_auth.expect_color_input_mail_is_red()

    def test_red_color_input_password(self, page_auth):
        page_auth.click_log_in()
        page_auth.expect_color_input_password_is_red()



class TestForgotPassword:

    def test_valid_forgot_password(self, page_auth):
        page_auth.click_on_forgot_password()
        mail = page_auth.input_mail_for_forgot_password()
        page_auth.click_on_reset_password()
        page_auth.expect_notification_valid_reset(mail)

    def test_forgot_password_empty_mail(self, page_auth):
        page_auth.click_on_forgot_password()
        page_auth.click_on_reset_password()
        page_auth.expect_notification_invalid_reset()

    def test_forgot_password_invalid_mail(self, page_auth):
        page_auth.click_on_forgot_password()
        mail = page_auth.input_invalid_mail()
        page_auth.click_on_reset_password()
        page_auth.expect_notification_invalid_reset(mail)


    def test_cancel_forgot_password(self, page_auth):
        page_auth.click_on_forgot_password()
        page_auth.click_cancel_forgot_password()

    def test_color_input_mail_forgot(self, page_auth):
        page_auth.click_on_forgot_password()
        page_auth.click_on_reset_password()
        page_auth.expect_color_input_mail_is_red()
