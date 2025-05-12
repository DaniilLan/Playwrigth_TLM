import time
import allure
import pytest


class TestAuth:

    # def test_create_user(self, auth_page, test_user):
    #     time.sleep(10)

    @allure.feature("Авторизация")
    @allure.title("Успешная авторизация админа Телемед")
    def test_log_in_admin_tele(self, auth_page):
        name_profile = auth_page.input_admin_tele()
        auth_page.input_valid_password()
        auth_page.click_log_in()
        auth_page.expect_valid_auth(name_profile)

    @allure.feature("Авторизация")
    @allure.title("Успешная авторизация админа Скорой")
    def test_log_in_admin_amb(self, auth_page):
        name_profile = auth_page.input_admin_amb()
        auth_page.input_valid_password()
        auth_page.click_log_in()
        auth_page.expect_valid_auth(name_profile)

    @allure.feature("Авторизация")
    @allure.title("Успешная авторизация админа ЦРБ")
    def test_log_in_admin_crb(self, auth_page):
        name_profile = auth_page.input_admin_crb()
        auth_page.input_valid_password()
        auth_page.click_log_in()
        auth_page.expect_valid_auth(name_profile)

    @allure.feature("Авторизация")
    @allure.title("Успешная авторизация врача Телемеда")
    def test_log_in_doctor_tele(self, auth_page):
        name_profile = auth_page.input_doctor_tele()
        auth_page.input_valid_password()
        auth_page.click_log_in()
        auth_page.expect_valid_auth(name_profile)

    @allure.feature("Авторизация")
    @allure.title("Успешная авторизация врача Скорой")
    def test_log_in_doctor_amb(self, auth_page):
        name_profile = auth_page.input_doctor_amb()
        auth_page.input_valid_password()
        auth_page.click_log_in()
        auth_page.expect_valid_auth(name_profile)

    @allure.feature("Авторизация")
    @allure.title("Успешная авторизация врача ЦРБ")
    def test_log_in_doctor_crb(self, auth_page):
        name_profile = auth_page.input_doctor_crb()
        auth_page.input_valid_password()
        auth_page.click_log_in()
        auth_page.expect_valid_auth(name_profile)

    @allure.feature("Авторизация")
    @allure.title("Указан неверный пароль")
    def test_invalid_password(self, auth_page):
        auth_page.input_doctor_crb()
        auth_page.input_invalid_password()
        auth_page.click_log_in()
        auth_page.expect_error_invalid_password()

    @allure.feature("Авторизация")
    @allure.title("Указана неверная почта")
    def test_invalid_mail(self, auth_page):
        auth_page.input_invalid_mail()
        auth_page.input_invalid_password()
        auth_page.click_log_in()
        auth_page.expect_error_invalid_mail()

    @allure.feature("Авторизация")
    @allure.title("Видимость основных элементов страницы")
    def test_visible_main_elements(self, auth_page):
        auth_page.expect_visible_all_elements()

    @allure.feature("Авторизация")
    @allure.title("Изменение плейсхолдера полей ввода при фокусе")
    def test_reducing_placeholder_on_click(self, auth_page):
        auth_page.expect_reducing_placeholder_mail()
        auth_page.expect_reducing_placeholder_password()

    @allure.feature("Авторизация")
    @allure.title("Скрыть/Показать пароль")
    def test_hide_show_password(self, auth_page):
        auth_page.expect_input_password_is_password()
        auth_page.click_eye_password()
        auth_page.expect_input_password_is_text()
        auth_page.click_eye_password()
        auth_page.expect_input_password_is_password()

    @allure.feature("Авторизация")
    @allure.title("Окраска поля mail при ошибке")
    def test_red_color_input_mail(self, auth_page):
        auth_page.click_log_in()
        auth_page.expect_color_input_mail_is_red()

    @allure.feature("Авторизация")
    @allure.title("Окраска поля password при ошибке")
    def test_red_color_input_password(self, auth_page):
        auth_page.click_log_in()
        auth_page.expect_color_input_password_is_red()

    @allure.feature("Восстановление пароля")
    @allure.title("Отправка ссылки по почте для восстановления пароля")
    def test_valid_forgot_password(self, auth_page):
        auth_page.click_on_link_forgot_password()
        mail = auth_page.input_mail_for_forgot_password()
        auth_page.click_on_reset_password()
        auth_page.expect_notification_valid_reset(mail)

    @allure.feature("Восстановление пароля")
    @allure.title("Отправка ссылки при пустом поле mail")
    def test_forgot_password_empty_mail(self, auth_page):
        auth_page.click_on_link_forgot_password()
        auth_page.click_on_reset_password()
        auth_page.expect_notification_invalid_reset()

    @allure.feature("Восстановление пароля")
    @allure.title("Отправка ссылки при несуществующем mail")
    def test_forgot_password_invalid_mail(self, auth_page):
        auth_page.click_on_link_forgot_password()
        mail = auth_page.input_invalid_mail()
        auth_page.click_on_reset_password()
        auth_page.expect_notification_invalid_reset(mail)

    @allure.feature("Восстановление пароля")
    @allure.title("Закрытие окна восстановления пароля")
    def test_cancel_forgot_password(self, auth_page):
        auth_page.click_on_link_forgot_password()
        auth_page.click_cancel_forgot_password()

    @allure.feature("Восстановление пароля")
    @allure.title("Окраска поля mail при ошибке (пустое поле ввода)")
    def test_red_color_input_mail_forgot(self, auth_page):
        auth_page.click_on_link_forgot_password()
        auth_page.click_on_reset_password()
        auth_page.expect_color_input_mail_is_red()

    @allure.feature("Восстановление пароля")
    @allure.title("Исчезновение кнопки 'Сбросить'")
    def test_disappearing_button_reset(self, auth_page):
        auth_page.click_on_link_forgot_password()
        auth_page.click_on_reset_password()
        auth_page.expect_color_input_mail_is_red()

    @allure.feature("Авторизация")
    @allure.title("Появление pop-up 'Обязательное поле' при наведении")
    def test_pop_up_hovering_input_field(self, auth_page):
        auth_page.click_log_in()
        auth_page.hovering_on_input_field_mail()
        auth_page.expect_visible_pop_up_required_email()
        auth_page.hovering_on_input_field_password()
        auth_page.expect_visible_pop_up_required_password()

    @allure.feature("Авторизация")
    @allure.title("Переход на страницу /help")
    def test_go_to_page_halp(self, auth_page):
        auth_page.click_on_link_help()
        auth_page.expect_valid_go_to_help_page()

    @allure.feature("Авторизация")
    @allure.title("Переход на страницу /support")
    def test_go_to_page_support(self, auth_page):
        auth_page.click_on_link_support()
        auth_page.expect_valid_go_to_support_page()

    @allure.feature("Восстановление пароля")
    @allure.title("Появление pop-up 'Обязательное поле' при наведении")
    def test_pop_up_hovering_input_field_forgot_password(self, auth_page):
        auth_page.click_on_link_forgot_password()
        auth_page.click_on_reset_password()
        auth_page.hovering_on_input_field_mail()
        auth_page.expect_visible_pop_up_required_email()

    @allure.feature("Авторизация")
    @allure.title("Рефреш страницы после клика по лого")
    def test_refresh_page_using_logo(self, auth_page):
        auth_page.click_on_logo()
        auth_page.expect_url_is_auth()