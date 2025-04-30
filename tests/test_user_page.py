from PageLocators.locators import *
import re
from config import *
import pytest
from Methods.db_method import QueryDB

db = QueryDB()

class TestPageUsers:
    @pytest.mark.parametrize('mail, name', [(mail, name) for mail, name in cred.items()])
    @pytest.mark.parametrize('password', [password_all])
    def test_auth(self, page_users, mail, password, name):
        page_users.login_users(mail, password)
        name_profile = page_users.get_texts(LocatorsPageUsers.NAME_PROFILE)
        assert name_profile == name
        page_users.screenshot(dop=mail)

    @pytest.mark.parametrize('mail', [mail_doc])
    @pytest.mark.parametrize('password', [password_all])
    def test_header_all_measurement(self, page_users, mail, password):
        page_users.login_users(mail, password)
        page_users.click(LocatorsPageUsers.BUTTON_HEADER_ALLMS)
        page_users.expect_visible_element(LocatorsPageAllMeasurements.TEXT_ALL_MEASUREMENTS)

    @pytest.mark.parametrize('mail', [mail_doc])
    @pytest.mark.parametrize('password', [password_all])
    def test_header_meetings(self, page_users, mail, password):
        page_users.login_users(mail, password)
        page_users.click(LocatorsPageUsers.BUTTON_HEADER_MEETING)
        page_users.expect_visible_elements(LocatorsPageMeetings.BUTTON_ADD_MEETING)

    @pytest.mark.parametrize('mail', [mail_doc])
    @pytest.mark.parametrize('password', [password_all])
    @pytest.mark.parametrize('locator', [LocatorsPageUsers.BUTTON_HEADER_USERS,
                                         LocatorsPageUsers.BUTTON_HEADER_ALLMS,
                                         LocatorsPageUsers.BUTTON_HEADER_MEETING,
                                         LocatorsPageUsers.BUTTON_ADD_USERS,
                                         LocatorsPageUsers.BELL])
    def test_button_role_doc(self, page_users, mail, password, locator):
        page_users.login_users(mail, password)
        page_users.expect_visible_elements(locator)

    @pytest.mark.parametrize('mail', mail_adm)
    @pytest.mark.parametrize('password', [password_all])
    @pytest.mark.parametrize('locator', [[LocatorsPageUsers.BUTTON_HEADER_USERS,
                                         LocatorsPageUsers.BUTTON_HEADER_ORGANIZATION,
                                         LocatorsPageUsers.BUTTON_HEADER_SETTINGS,
                                         LocatorsPageUsers.BUTTON_LOGS_AUDIT,
                                         LocatorsPageUsers.BUTTON_LOAD_PATIENT,
                                         LocatorsPageUsers.BUTTON_ADD_USERS]])
    def test_button_role_adm(self, page_users, mail, password, locator):
        page_users.login_users(page_users, mail, password)
        page_users.expect_visible_elements(locator)

    @pytest.mark.parametrize("mail, password", [
        (mail_adm, password_all),
        (mail_doc, password_all),
    ], ids=[
        "for_admim",
        "for_doctor"
    ])
    def test_name_title_page(self, page_users, mail, password):
        page_users.login_users(mail, password)
        element = LocatorsPageUsers.USERS_OR_PATIENTS
        page_users.wait_visible_elements(element)
        text = page_users.get_text(element)
        if mail in mails_adm:
            assert "Пользователи" in text
        elif mail in mails_doc:
            assert "Пациенты" in text

    @pytest.mark.parametrize('mail', [mail for mail in cred])
    @pytest.mark.parametrize('password', [password_all])
    def test_quantity_users(self, page_users, mail, password):
        page_users.login_users(mail, password)
        head_quantity = page_users.get_text(LocatorsPageUsers.QUANTITY_USERS_HEADER)
        pag_quantity = page_users.get_text(LocatorsPageUsers.QUANTITY_USERS_PAGINATION)
        top = head_quantity.strip('()')
        bot = re.split("из ", pag_quantity)
        assert bot[1] == top

    @pytest.mark.parametrize('mail', [mail for mail in cred])
    @pytest.mark.parametrize('password', [password_all])
    def test_drop_filter(self, page_users, mail, password):
        page_users.login_users(mail, password)
        page_users.click(LocatorsPageUsers.DROPDOWN_FILTER)

    @pytest.mark.parametrize('mail', [mail for mail in cred])
    @pytest.mark.parametrize('password', [password_all])
    def test_boxs_input_filter(self, page_users, mail, password):
        page_users.login_users(mail, password)
        page_users.dropdown_filter()
        page_users.focus_inputs(LocatorsPageUsers.FILTER_INPUT_BOXS)

    @pytest.mark.parametrize('mail', [mail for mail in cred])
    @pytest.mark.parametrize('password', [password_all])
    def test_boxs_dropdown_filter(self, page_users, mail, password):
        page_users.login_users(mail, password)
        page_users.dropdown_filter()
        page_users.click(LocatorsPageUsers.FILTER_DROPDOWN_GENDER)
        page_users.wait_visible_elements(LocatorsPageUsers.FILTER_LIST_GENDER)
        page_users.click(LocatorsPageUsers.FILTER_DROPDOWN_ORG)
        page_users.wait_visible_elements(LocatorsPageUsers.FILTER_LIST_ORG_ROLE)
        if mail in mails_adm:
            page_users.click(LocatorsPageUsers.FILTER_DROPDOWN_ROLE)
            page_users.wait_visible_elements(LocatorsPageUsers.FILTER_DROPDOWN_ROLE)


    # class TestPagination:
    #
    #     @pytest.mark.parametrize('mail', [mail for mail in mails_doc])
    #     @pytest.mark.parametrize('password', [password_all])
    #     @pytest.mark.parametrize('limit', [LocatorsPageUsers.PAGINATION_20,
    #                                        LocatorsPageUsers.PAGINATION_50,
    #                                        LocatorsPageUsers.PAGINATION_100,
    #                                        LocatorsPageUsers.PAGINATION_150]) ----------------------------------------- Предусловие: должно быть более 150 пользователей
    #     def test_quantity_user_limit(self, page_users, limit, mail, password):
    #         page_users.login_users(mail, password)
    #         page_users.click(limit)
    #         quantity_pagination = page_users.get_text(limit)
    #         quantity_users = page_users.get_quantity_elements(LocatorsPageUsers.USERS_LIST)
    #         assert quantity_users == int(quantity_pagination)
    #         page_users.click(LocatorsPageUsers.BUTTON_HEADER_ALLMS)

    class TestChangePassword:

        def test_valid_change_password(self, page_users, test_user):
            page_users.login_users(test_user['mail'], test_user['password'])
            page_users.click(LocatorsPageUsers.NAME_PROFILE)
            page_users.click(LocatorsPageUsers.BUTTON_CHANGE_PASSWORD)
            page_users.change_password(test_user['password'], invalid_pass)
            page_users.click(LocatorsPageUsers.BUTTON_SAVE_NEW_PASS)
            page_users.wait_visible_elements(LocatorsGeneral.NOTIFICATION_ALL)
            notif_text = page_users.get_text(LocatorsGeneral.NOTIFICATION_ALL)
            assert notif_text == "Пароль успешно изменён"
            page_users.wait_until_visible_elements(LocatorsGeneral.NOTIFICATION_ALL)

        def test_current_password_invalid(self, page_users, test_user):
            page_users.login_users(test_user['mail'], test_user['password'])
            page_users.click(LocatorsPageUsers.NAME_PROFILE)
            page_users.click(LocatorsPageUsers.BUTTON_CHANGE_PASSWORD)
            page_users.change_password("98763578", invalid_pass)
            page_users.click(LocatorsPageUsers.BUTTON_SAVE_NEW_PASS)
            page_users.wait_visible_elements(LocatorsGeneral.NOTIFICATION_ALL)
            notif_text = page_users.get_text(LocatorsGeneral.NOTIFICATION_ALL)
            assert notif_text == "Пароль не верный."
            page_users.wait_until_visible_elements(LocatorsGeneral.NOTIFICATION_ALL)

        def test_empty_new_password(self, page_users, test_user):
            page_users.login_users(test_user['mail'], test_user['password'])
            page_users.click(LocatorsPageUsers.NAME_PROFILE)
            page_users.click(LocatorsPageUsers.BUTTON_CHANGE_PASSWORD)
            page_users.fill_text(LocatorsPageUsers.INPUT_CURRENT_PASS, test_user["password"])
            page_users.fill_text(LocatorsPageUsers.INPUT_NEW_PASS, "123")
            page_users.fill_text(LocatorsPageUsers.INPUT_NEW2_PASS, "")
            page_users.click(LocatorsPageUsers.BUTTON_SAVE_NEW_PASS)
            page_users.wait_visible_elements(LocatorsGeneral.NOTIFICATION_ALL)
            notif_text = page_users.get_text(LocatorsGeneral.NOTIFICATION_ALL)
            assert notif_text == "Пароль не может быть изменён"
            page_users.wait_until_visible_elements(LocatorsGeneral.NOTIFICATION_ALL)


        @pytest.mark.parametrize('mail', [mail_doc])
        @pytest.mark.parametrize('password', [password_all])
        @pytest.mark.parametrize('body_input', [[LocatorsPageUsers.INPUT_CURRENT_PASS,
                                                 LocatorsPageUsers.INPUT_NEW_PASS,
                                                 LocatorsPageUsers.INPUT_NEW2_PASS]])
        @pytest.mark.parametrize('placeholder_input', [[LocatorsPageUsers.PLACEHOLDER_CURRENT_PASS,
                                                        LocatorsPageUsers.PLACEHOLDER_NEW_PASS,
                                                        LocatorsPageUsers.PLACEHOLDER_NEW2_PASS]])
        def test_color_input_change_password(self, page_users, mail, password, body_input, placeholder_input):
            page_users.login_users(mail, password)
            page_users.click(LocatorsPageUsers.NAME_PROFILE)
            page_users.click(LocatorsPageUsers.BUTTON_CHANGE_PASSWORD)
            page_users.click(LocatorsPageUsers.BUTTON_SAVE_NEW_PASS)
            page_users.expect_invalid_input_color(placeholder_input, body_input)
            page_users.wait_visible_elements(LocatorsGeneral.NOTIFICATION_ALL)
            notif_text = page_users.get_text(LocatorsGeneral.NOTIFICATION_ALL)
            assert notif_text == "Пароль не может быть изменён"
            page_users.wait_until_visible_elements(LocatorsGeneral.NOTIFICATION_ALL)

    class TestChangeProfile:

        @pytest.mark.parametrize('mail', [mail_doc])
        @pytest.mark.parametrize('password', [password_all])
        @pytest.mark.parametrize('body_input', [[LocatorsPageUsers.INPUT_CHANGE_F,
                                                 LocatorsPageUsers.INPUT_CHANGE_I,
                                                 LocatorsPageUsers.INPUT_CHANGE_MAIL,
                                                 LocatorsPageUsers.INPUT_CHANGE_PHONE]])
        @pytest.mark.parametrize('placeholder_input', [[LocatorsPageUsers.PLACEHOLDER_CHANGE_F,
                                                        LocatorsPageUsers.PLACEHOLDER_CHANGE_I,
                                                        LocatorsPageUsers.PLACEHOLDER_CHANGE_MAIL,
                                                        LocatorsPageUsers.PLACEHOLDER_CHANGE_PHONE]])
        def test_empty_input_change_profile(self, page_users, mail, password, body_input, placeholder_input):
            page_users.login_users(mail, password)
            page_users.click(LocatorsPageUsers.NAME_PROFILE)
            page_users.click(LocatorsPageUsers.BUTTON_CHANGE_PROFILE)
            page_users.clear_inputs(body_input)
            page_users.click(LocatorsPageUsers.BUTTON_SAVE_PROFILE)
            text_notif = page_users.get_text(LocatorsGeneral.NOTIFICATION_ALL)
            assert text_notif == "Ошибка при изменении пользователя"
            page_users.wait_until_visible_elements(LocatorsGeneral.NOTIFICATION_ALL)

        @pytest.mark.parametrize('mail', [mail_doc])
        @pytest.mark.parametrize('password', [password_all])
        @pytest.mark.parametrize('body_input', [[LocatorsPageUsers.INPUT_CHANGE_F,
                                                 LocatorsPageUsers.INPUT_CHANGE_I,
                                                 LocatorsPageUsers.INPUT_CHANGE_MAIL,
                                                 LocatorsPageUsers.INPUT_CHANGE_PHONE]])
        @pytest.mark.parametrize('placeholder_input', [[LocatorsPageUsers.PLACEHOLDER_CHANGE_F,
                                                        LocatorsPageUsers.PLACEHOLDER_CHANGE_I,
                                                        LocatorsPageUsers.PLACEHOLDER_CHANGE_MAIL,
                                                        LocatorsPageUsers.PLACEHOLDER_CHANGE_PHONE]])
        def test_color_required_field_change_profile(self, page_users, mail, password, body_input, placeholder_input):
            page_users.login_users(mail, password)
            page_users.click(LocatorsPageUsers.NAME_PROFILE)
            page_users.click(LocatorsPageUsers.BUTTON_CHANGE_PROFILE)
            page_users.clear_inputs(body_input)
            page_users.click(LocatorsPageUsers.BUTTON_SAVE_PROFILE)
            page_users.expect_invalid_input_color(placeholder_input, body_input)
            page_users.wait_until_visible_elements(LocatorsGeneral.NOTIFICATION_ALL)

        @pytest.mark.parametrize('mail', [mail_doc])
        @pytest.mark.parametrize('password', [password_all])
        def test_close_change_profile(self, page_users, mail, password):
            page_users.login_users(mail, password)
            page_users.click(LocatorsPageUsers.NAME_PROFILE)
            page_users.click(LocatorsPageUsers.BUTTON_CHANGE_PROFILE)
            page_users.click(LocatorsPageUsers.BUTTON_X_CHANGE_PROFILE)
            page_users.expect_not_visible_elements(LocatorsPageUsers.WINDOW_CHANGE_PROFILE)
#------------------------------------------------------------------------------------------------------------------------ Почти
    class TestAddUsers:

        @pytest.mark.parametrize('mail', ['mailtest@mail.ru'])
        @pytest.mark.parametrize('org_id', [100, 101, 102, 103])
        @pytest.mark.parametrize('password', [password_all])
        def test_valid_add_user_required_field(self, page_users, mail, password, org_id):
            access_token = page_users.api_get_access_token_adm(org_id)
            user_id = page_users.api_create_doctor(mail, password, access_token, org_id)
            page_users.login_users(page_users, mail, password)
            page_users.click(LocatorsPageUsers.BUTTON_ADD_USERS)
            page_users.fill_text(LocatorsPageUsers.INPUT_ADD_USER_F, random_fio('F'))
            page_users.fill_text(LocatorsPageUsers.INPUT_ADD_USER_I, random_fio('I'))
            page_users.fill_text(LocatorsPageUsers.INPUT_ADD_USER_DATA, random_data())
            page_users.click(LocatorsPageUsers.INPUT_ADD_USER_ORG)
            page_users.open_dropdown_organization()
            page_users.click(LocatorsPageUsers.ORG_TELCENT_AMBULANCE_CRB1_FAP1)
            page_users.click(LocatorsPageUsers.BUTTON_ADD_USER_IN_WINDOW)
            notification = page_users.GeneralLocators.NOTIFICATION_ALL
            page_users.wait_visible_elements(notification)
            assert page_users.get_texts(notification) == "Пользователь успешно добавленДиагнозы успешно изменены"
            page_users.expect_visible_elements(LocatorsPageUsers.DIV_SUCCESSFULLY_CREATED)
            page_users.wait_until_visible_elements(notification)
            page_users.api_delete_user(user_id, access_token)

        @pytest.mark.parametrize('mail', [mail_doc])
        @pytest.mark.parametrize('password', [password_all])
        def test_valid_add_user_all_field(self, page_users, mail, password):
            page_users.login_users(page_users, mail, password)
            page_users.click(LocatorsPageUsers.BUTTON_ADD_USERS)
            page_users.fill_text(LocatorsPageUsers.INPUT_ADD_USER_F, random_fio('F'))
            page_users.fill_text(LocatorsPageUsers.INPUT_ADD_USER_I, random_fio('I'))
            page_users.fill_text(LocatorsPageUsers.INPUT_ADD_USER_O, random_fio('O'))
            page_users.fill_text(LocatorsPageUsers.INPUT_ADD_USER_DATA, random_data())
            page_users.fill_text(LocatorsPageUsers.INPUT_ADD_USER_HEIGHT, random_height_weight())
            page_users.fill_text(LocatorsPageUsers.INPUT_ADD_USER_WEIGHT, random_height_weight())
            page_users.fill_text(LocatorsPageUsers.INPUT_ADD_USER_MAIL, random_mail())
            page_users.fill_text(LocatorsPageUsers.INPUT_ADD_USER_PHONE, random_phone())
            page_users.click(LocatorsPageUsers.INPUT_ADD_USER_ORG)
            page_users.open_dropdown_organization()
            page_users.click(LocatorsPageUsers.ORG_TELCENT_AMBULANCE_CRB1_FAP1)
            page_users.click(LocatorsPageUsers.INPUT_ADD_USER_DIAGNOSES)
            page_users.click(LocatorsPageUsers.INPUT_ADD_USER_DIAGNOSES_CHOOSE_ALL)
            page_users.click(LocatorsPageUsers.BUTTON_ADD_USER_IN_WINDOW)
            notification = page_users.GeneralLocators.NOTIFICATION_ALL
            page_users.wait_visible_elements(notification)
            assert page_users.get_texts(notification) == "Пользователь успешно добавленДиагнозы успешно изменены"
            page_users.expect_visible_elements(LocatorsPageUsers.DIV_SUCCESSFULLY_CREATED)
            page_users.wait_until_visible_elements(notification)

        @pytest.mark.parametrize('mail', [mail_doc])
        @pytest.mark.parametrize('password', [password_all])
        @pytest.mark.parametrize('body_input', [[LocatorsPageUsers.INPUT_ADD_USER_F,
                                                LocatorsPageUsers.INPUT_ADD_USER_I,
                                                LocatorsPageUsers.INPUT_ADD_USER_DATA,
                                                LocatorsPageUsers.INPUT_ADD_USER_ORG]])
        @pytest.mark.parametrize('placeholder_input', [[LocatorsPageUsers.PLACEHOLDER_ADD_USER_F,
                                                        LocatorsPageUsers.PLACEHOLDER_ADD_USER_I,
                                                        LocatorsPageUsers.PLACEHOLDER_ADD_USER_DATA,
                                                        LocatorsPageUsers.PLACEHOLDER_ADD_USER_ORG]])
        def test_empty_input_field_add_user(self, page_users, mail, password, body_input, placeholder_input):
            page_users.login_users(page_users, mail, password)
            page_users.click(LocatorsPageUsers.BUTTON_ADD_USERS)
            page_users.click(LocatorsPageUsers.BUTTON_ADD_USER_IN_WINDOW)
            page_users.expect_invalid_input_color(placeholder_input, body_input)
            notification = page_users.GeneralLocators.NOTIFICATION_ALL
            text_notification = page_users.get_texts(notification)
            assert text_notification == "Заполните все обязательные поля"
            page_users.wait_until_visible_elements(notification)
