from locators.base_locators import LocatorsBase
from locators.auth_locators import LocatorsAuth

import pytest


@pytest.mark.usefixtures("page")
class TestPageAuth:

    # @pytest.mark.parametrize('elements', LocatorsBase.base_elements)
    # def test_visible_auth_elements(self, elements):
    #     self.page.wait_visible_elements(elements)

    # @pytest.mark.parametrize('elements', LocatorsAuth.auth_elements)
    # def test_visible_base_elements(self, elements):
    #     self.page.wait_visible_elements(elements)

    # @pytest.mark.parametrize("mail, password, expected_error", [
    #     # Валидная почта + неверный пароль
    #     (mail_doc_tele, "1278", "Неверный пароль!"),
    #     # Невалидная почта + любой пароль
    #     (invalid_mail, "1278", "Имя пользователя или пароль не верные."),
    # ], ids=[
    #     "valid_email_wrong_password",
    #     "invalid_email_any_password"
    # ])
    # def test_invalid_auth(self, mail, password, expected_error):
    #     self.page.fill_text(LocatorsAuth.INPUT_MAIL, mail)
    #     self.page.fill_text(LocatorsAuth.INPUT_PASSWORD, password)
    #     self.page.click(LocatorsAuth.BUTTON_LOG)
    #     self.page.wait_visible_elements(LocatorsBase.NOTIFICATION_ALL)
    #     self.page.expect_text(LocatorsBase.NOTIFICATION_ALL, expected_error)

#     def test_focus_input_mail(self, page_auth):
#         page_auth.focus_element(LocatorsAuth.INPUT_MAIL)
#
#     def test_focus_input_pass(self, page_auth):
#         page_auth.focus_element(LocatorsAuth.INPUT_PASSWORD)
#
#     def test_placeholder_before_click(self, page_auth):
#         page_auth.click(LocatorsAuth.INPUT_MAIL)
#         page_auth.expect_visible_elements(LocatorsAuth.PLACEHOLDER_EMAIL)
#         type_class_mail = page_auth.get_attribute_element(LocatorsAuth.DIV_INPUT_EMAIL, 'class')
#         assert 'focused__e6b9' in type_class_mail
#         page_auth.click(LocatorsAuth.INPUT_PASSWORD)
#         page_auth.expect_visible_elements(LocatorsAuth.PLACEHOLDER_PASSWORD)
#         type_class_pass = page_auth.get_attribute_element(LocatorsAuth.DIV_INPUT_PASS, 'class')
#         assert 'focused__e6b9' in type_class_pass
#
#     def test_type_password(self, page_auth):
#         page_auth.fill_text(LocatorsAuth.INPUT_PASSWORD, "12345678")
#         assert page_auth.get_attribute_element(LocatorsAuth.INPUT_PASSWORD, 'type') == 'password'
#
#     def test_ear_password(self, page_auth):
#         page_auth.fill_text(LocatorsAuth.INPUT_PASSWORD, "12345678")
#         page_auth.click(LocatorsAuth.EYE_PASSWORD)
#         assert page_auth.get_attribute_element(LocatorsAuth.INPUT_PASSWORD, 'type') == 'text'
#         page_auth.click(LocatorsAuth.EYE_PASSWORD)
#         assert page_auth.get_attribute_element(LocatorsAuth.INPUT_PASSWORD, 'type') == 'password'
#
#     def test_color_input_mail(self, page_auth):
#         page_auth.click(LocatorsAuth.BUTTON_LOG)
#         color_text = LocatorsAuth.PLACEHOLDER_EMAIL
#         border_background_color = LocatorsAuth.INPUT_MAIL
#         page_auth.expect_invalid_input_color(color_text, border_background_color)
#
#     def test_color_input_password(self, page_auth):
#         page_auth.click(LocatorsAuth.BUTTON_LOG)
#         color_text = LocatorsAuth.PLACEHOLDER_PASSWORD
#         border_background_color = LocatorsAuth.INPUT_PASSWORD
#         page_auth.expect_invalid_input_color(color_text, border_background_color)
#
# class TestForgotPassword:
#
#     def test_valid_forgot_password(self, page_auth):
#         page_auth.click(LocatorsAuth.LINK_FORGOT_PASSWORD)
#         page_auth.expect_visible_elements(LocatorsAuth.PLACEHOLDER_EMAIL)
#         page_auth.fill_text(LocatorsAuth.INPUT_MAIL, "landan2001@mail.ru")
#         page_auth.click(LocatorsAuth.BUTTON_FORGOT)
#         page_auth.wait_until_visible_elements(LocatorsBase.NOTIFICATION_ALL)
#
#     @pytest.mark.parametrize("mail", ["", invalid_mail],
#                              ids=[
#                                  "empty_email_forgot_password",
#                                  "invalid_email_forgot_password"
#                              ])
#     def test_forgot_password(self, page_auth, mail):
#         page_auth.click(LocatorsAuth.LINK_FORGOT_PASSWORD)
#         page_auth.expect_visible_elements(LocatorsAuth.PLACEHOLDER_EMAIL)
#         page_auth.fill_text(LocatorsAuth.INPUT_MAIL, mail)
#         page_auth.click(LocatorsAuth.BUTTON_FORGOT)
#         page_auth.wait_visible_elements(LocatorsBase.NOTIFICATION_ALL)
#         text_notif = page_auth.get_text(LocatorsBase.NOTIFICATION_ALL)
#         if mail == '':
#             assert text_notif == "Отсутствует обязательное поле email!"
#             page_auth.wait_until_visible_elements(LocatorsBase.NOTIFICATION_ALL)
#         elif mail == invalid_mail:
#             assert text_notif == f"Пользователь c логином '{invalid_mail}' не существует!"
#             page_auth.wait_until_visible_elements(LocatorsBase.NOTIFICATION_ALL)
#
#     def test_cancel_forgot_password(self, page_auth):
#         page_auth.click(LocatorsAuth.LINK_FORGOT_PASSWORD)
#         page_auth.click(LocatorsAuth.BUTTON_CANCEL)
#         page_auth.expect_visible_elements(LocatorsAuth.BUTTON_LOG)
#
    def test_color_input_mail_forgot(self):
        self.page.click(LocatorsAuth.LINK_FORGOT_PASSWORD)
        self.page.click(LocatorsAuth.BUTTON_LOG)
        color_text = LocatorsAuth.PLACEHOLDER_EMAIL
        border_background_color = LocatorsAuth.INPUT_MAIL
        self.page.expect_invalid_input_color(color_text, border_background_color)
