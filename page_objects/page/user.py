import time

from page_objects.base_page import BasePage
from page_objects.page.auth import LocatorsAuth


class LocatorsUsers:
    BUTTON_ADD_USER_IN_WINDOW = '//html/body/div[2]/div/div[2]/form/div[2]/button'
    POPUP_PROFILE = '//html/body/div[2]/div'
    NAME_PROFILE = '//*[@id="rootTelemedHub"]//div/div/div[2]/strong'
    BUTTON_CHANGE_PASSWORD = 'div[data-locator="openChangePassword"]'
    BUTTON_CHANGE_PROFILE = 'div[data-locator="openChangeProfile"]'
    INPUT_CURRENT_PASS = '//html/body/div[2]/div/div[2]/form/div[1]/div/div/div/input'
    PLACEHOLDER_CURRENT_PASS = '//html/body/div[2]/div/div[2]/form/div[1]/div/div/label'
    INPUT_NEW_PASS = '//html/body/div[2]/div/div[2]/form/div[2]/div/div/div/input'
    PLACEHOLDER_NEW_PASS = '//html/body/div[2]/div/div[2]/form/div[2]/div/div/label'
    INPUT_NEW2_PASS = '//html/body/div[2]/div/div[2]/form/div[3]/div/div/div/input'
    PLACEHOLDER_NEW2_PASS = '//html/body/div[2]/div/div[2]/form/div[3]/div/div/label'
    BUTTON_SAVE_NEW_PASS = '//html/body/div[2]/div/div[2]/form/button'
    BUTTON_HEADER_USERS = "a[data-locator='/users']"
    BUTTON_HEADER_ALLMS = "a[data-locator='/all-measurements']"
    BUTTON_HEADER_MEETING = "a[data-locator='/meetings']"
    BUTTON_HEADER_ORGANIZATION = "a[data-locator='/organizations']"
    BUTTON_HEADER_SETTINGS = "a[data-locator='/settings']"
    BUTTON_LOGS_AUDIT = '//div[2]/main/div/div[1]/div[2]/button[1]'
    BUTTON_LOAD_PATIENT = '//div[2]/main/div/div[1]/div[2]/button[2]'
    BUTTON_ADD_USERS = '//button[@data-locator="addUser"]'
    USERS_OR_PATIENTS = "//div[2]/main/div/div[1]/div[1]"
    QUANTITY_USERS_HEADER = "//div[2]/main/div/div[1]/div[1]/span"
    QUANTITY_USERS_PAGINATION = "//*[@id='rootTelemedHub']/div[2]/main/div/div[3]/div[3]/div[3]"
    DROPDOWN_FILTER = '//*[@id="rootTelemedHub"]/div[2]/main/div/div[2]/label'
    BUTTON_APPLY_FILTER = 'button[data-locator="apply"]'
    FILTER_FORM = 'div[class="filterForm__PexX"]'
    FILTER_INPUT_BOXS = '//div/div/input'
    FILTER_DROPDOWN_DIV = '//*[@id="rootTelemedHub"]/div[2]/main/div/div[2]/div/div'
    FILTER_DROPDOWN_GENDER = '//*[@id="rootTelemedHub"]/div[2]/main/div/div[2]/div/div/div/div[5]/div/div/div[2]'
    FILTER_LIST_GENDER = '//html/body/div[2]/ul'
    FILTER_DROPDOWN_ROLE = '//*[@id="rootTelemedHub"]/div[2]/main/div/div[2]/div/div/div/div[7]/div/div'
    FILTER_DROPDOWN_ORG = '//*[@id="rootTelemedHub"]/div[2]/main/div/div[2]/div/div/div/div[6]/div/div'
    ORGS_IN_DROPDOWN_LIST = '//div[@class="arrowControl__e920 arrowControl"]'
    FILTER_LIST_ORG_ROLE = '//html/body/div[2]/div'
    PAGINATION_20 = '//div[@class="limitsList__IzFN"]/span[1]'
    PAGINATION_50 = '//div[@class="limitsList__IzFN"]/span[2]'
    PAGINATION_100 = '//div[@class="limitsList__IzFN"]/span[3]'
    PAGINATION_150 = '//div[@class="limitsList__IzFN"]/span[4]'
    USERS_LIST = '//div[@class="UsersList__E2xs"]/div'
    BELL = '//div[@class="NotificationDropdownHeader__sFmv"]'
    INPUT_CHANGE_F = '//html/body/div[2]/div/div[2]/form/div[1]/div/div/input'
    INPUT_CHANGE_I = '//html/body/div[2]/div/div[2]/form/div[2]/div/div/div/input'
    INPUT_CHANGE_O = '//html/body/div[2]/div/div[2]/form/div[3]/div/div/div/input'
    INPUT_CHANGE_MAIL = '//html/body/div[2]/div/div[2]/form/div[4]/div/div/div/input'
    INPUT_CHANGE_PHONE = '//div[label[text()="Телефон"]]//input'
    PLACEHOLDER_CHANGE_F = '//div[@data-locator="lastName"]/div/label[text()="Фамилия"]'
    PLACEHOLDER_CHANGE_I = '//div[@data-locator="firstName"]/div/div/label[text()="Имя"]'
    PLACEHOLDER_CHANGE_O = '//div[@data-locator="middleName"]/div/div/label[text()="Отчество"]'
    PLACEHOLDER_CHANGE_MAIL = '//div[@data-locator="email"]/div/div/label[text()="Email"]'
    PLACEHOLDER_CHANGE_PHONE = '//div[@data-locator="phone"]/div/div/label[text()="Телефон"]'
    BUTTON_SAVE_PROFILE = '//html/body/div[2]/div/div[2]/form/button'
    DOCTORS = "//div[div[span[text()='Врачи']]]//div[@class='gm_s']"
    WINDOW_CHANGE_PROFILE = '//div[@class="WrapModal productTheme__ef49 WrapModal__b7af"]'
    BUTTON_X_CHANGE_PROFILE = "//html/body/div[2]/div/div[1]/div"
    INPUT_ADD_USER_F = '//html/body/div[2]/div/div[2]/form/div[1]/div[1]/div/input'
    INPUT_ADD_USER_I = '//html/body/div[2]/div/div[2]/form/div[1]/div[2]/div/input'
    INPUT_ADD_USER_O = '//html/body/div[2]/div/div[2]/form/div[1]/div[3]/div/input'
    INPUT_ADD_USER_DATA = '//html/body/div[2]/div/div[2]/form/div[1]/div[4]/div/div/div/div/input'
    INPUT_ADD_USER_HEIGHT = '//html/body/div[2]/div/div[2]/form/div[1]/div[6]/div/input'
    INPUT_ADD_USER_WEIGHT = '//html/body/div[2]/div/div[2]/form/div[1]/div[7]/div/input'
    INPUT_ADD_USER_MAIL = '//html/body/div[2]/div/div[2]/form/div[1]/div[8]/div/input'
    INPUT_ADD_USER_PHONE = '//html/body/div[2]/div/div[2]/form/div[1]/div[9]/div/input'
    INPUT_ADD_USER_ORG = '//html/body/div[2]/div/div[2]/form/div[1]/div[11]/div/div/div/input'
    INPUT_ADD_USER_DIAGNOSES = '//html/body/div[2]/div/div[2]/form/div[1]/div[12]/div/div'
    INPUT_ADD_USER_DIAGNOSES_CHOOSE_ALL = '//html/body/div[3]/div/div[2]/div[1]'
    PLACEHOLDER_ADD_USER_F = "//div[@data-locator='WrapModal']//label[text()='Фамилия']"
    PLACEHOLDER_ADD_USER_I = "//div[@data-locator='WrapModal']//label[text()='Имя']"
    PLACEHOLDER_ADD_USER_DATA = "//div[@data-locator='WrapModal']//label[text()='Дата рождения']"
    PLACEHOLDER_ADD_USER_ORG = "//div[@data-locator='WrapModal']//label[text()='Организация']"
    PLACEHOLDER_ADD_USER_PHONE = "//div[@data-locator='WrapModal']//label[text()='Телефон']"
    PLACEHOLDER_ADD_USER_MAIL = "//div[@data-locator='WrapModal']//label[text()='E-mail']"
    DIV_SUCCESSFULLY_CREATED = '//div[@data-locator="credentialUser"]'
    ORG_LVL0 = '//html/body/div[3]/div/div/div[1]/div[2]'
    ORG_LVL1 = '//html/body/div[3]/div/div/div[2]/div/div/div[1]/div[2]'
    ORG_LVL2 = '//html/body/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[2]'
    ORG_LVL3 = '//html/body/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div'
    INPUT_FILTER_F = "//label[contains(text(),'Фамилия')]/following-sibling::div//input"
    KEBAB_MENU_USER_AVTOTEST = '//div[div/div/div[text()="АвтоТестов АвтоТест "]]//div[@class="controlViewBtn__UeJ4"]'
    BUTTON_PARAMS_USER_AVTOTEST = '//div[div/div/div[text()="АвтоТестов АвтоТест "]]//div[@class="containerSlide__AhIP"]//div/button[span[text()="Показатели пациента"]]'
    XCH_BUTTON_MODUL = '//button[span[text()="Модуль ХСН"]]'
    XCH_TRIANGLE_MAIN_DIAGNOSIS = '//div[label[text()="Основной диагноз"]]/div[@data-locator="SelectAfter"]'
    XCH_TRIANGLE_CLARIFYING_DIAGNOSIS = '//div[label[text()="Уточняющий диагноз"]]/div[@data-locator="SelectAfter"]'
    XCH_TRIANGLE_STAGE = '//div[label[text()="Стадия ХСН"]]/div[@data-locator="SelectAfter"]'
    XCH_MAIN_DIAGNOSIS_150 = '//li[@data-locator="optionI50"]'
    XCH_CLARIFYING_DIAGNOSIS_150_0 = '//li[@data-locator="optionI50.0"]'
    XCH_STAGE_I = '//li[@data-locator="optionstageI"]'
    XCH_BUTTON_NEXT = '//button[span[text()="Далее"]]'
    XCH_ALL_CHECK_BOXS = '//label[@data-locator="checkBoxLabel"]'
    XCH_ALL_TRIANGLES_SECOND_COLLECTION = '//div[@class="CcrsQuestionnaireForm__gyFw"]//div[@data-locator="SelectAfter"]'
    XCH_ANSWERS_0 = '//li[@data-locator="optionno"]'
    XCH_ANSWER_BODY_POSITION_0 = '//li[@data-locator="optionhorizontal"]'
    XCH_ANSWER_LIVER_0 = '//li[@data-locator="optionnotEnlarged"]'
    XCH_ANSWER_LVL_SAD_0 = '//li[@data-locator="optionhigher"]'
    XCH_INPUT_METERS = '//div[label[text()="Метры"]]/div/input[@data-locator="input"]'
    XCH_BUTTON_CALCULATE = '//button[span[text()="Рассчитать"]]'



    required_fields_change_profile = [INPUT_CHANGE_F,
                                      INPUT_CHANGE_I,
                                      INPUT_CHANGE_MAIL,
                                      INPUT_CHANGE_PHONE]
    placeholders_required_fields_change_profile = [PLACEHOLDER_CHANGE_F,
                                                   PLACEHOLDER_CHANGE_I,
                                                   PLACEHOLDER_CHANGE_MAIL,
                                                   PLACEHOLDER_CHANGE_PHONE]
    lvl_orgs = [ORG_LVL0,
                ORG_LVL1,
                ORG_LVL2,
                ORG_LVL3]


class UsersPage(BasePage):

    def log_in_doctor_tele(self):
        self.log_in(self.conf.creds.doctor_tele,
                    LocatorsAuth.INPUT_MAIL,
                    LocatorsAuth.INPUT_PASSWORD,
                    LocatorsAuth.BUTTON_LOGIN)

    def dropdown_filter(self):
        """Опустить drop-down список 'Фильтры' - изменив параметр элемента в DOM"""
        element = self.page.locator(LocatorsUsers.FILTER_DROPDOWN_DIV)
        element.evaluate('(element) => { element.style.maxHeight = "none"; }')

    def open_all_dropdown_organization(self):
        """Раскрыть все видимые организации в поле 'Организации' при добавлении пользователя"""
        self.page.click(LocatorsUsers.FILTER_DROPDOWN_ORG)
        elements = self.page.locator(LocatorsUsers.ORGS_IN_DROPDOWN_LIST).all()
        col = 0
        while col != len(elements):
            self.click(LocatorsUsers.ORGS_IN_DROPDOWN_LIST)
            col += 1

    def change_password(self, current_pass: str, new_pass: str):
        """Смена пароля на стр. /users в профиле пользователя"""
        self.fill_text(LocatorsUsers.INPUT_CURRENT_PASS, current_pass)
        self.fill_text(LocatorsUsers.INPUT_NEW_PASS, new_pass)
        self.fill_text(LocatorsUsers.INPUT_NEW2_PASS, new_pass)

    def search_user_filter(self):
        self.fill_text(LocatorsUsers.INPUT_FILTER_F, 'АвтоТест')
        self.click(LocatorsUsers.BUTTON_APPLY_FILTER)

    def select_user_for_XCH(self):
        self.click(LocatorsUsers.KEBAB_MENU_USER_AVTOTEST)
        self.click(LocatorsUsers.BUTTON_PARAMS_USER_AVTOTEST)

    def open_user_modul_XCH(self):
        self.click(LocatorsUsers.XCH_BUTTON_MODUL)

    def select_main_diagnosis_XCH(self):
        self.click(LocatorsUsers.XCH_TRIANGLE_MAIN_DIAGNOSIS)
        self.click(LocatorsUsers.XCH_MAIN_DIAGNOSIS_150)

    def select_clarifying_diagnosis_XCH(self):
        self.click(LocatorsUsers.XCH_TRIANGLE_CLARIFYING_DIAGNOSIS)
        self.click(LocatorsUsers.XCH_CLARIFYING_DIAGNOSIS_150_0)

    def select_stage_XCH(self):
        self.click(LocatorsUsers.XCH_TRIANGLE_STAGE)
        self.click(LocatorsUsers.XCH_STAGE_I)

    def save_first_collecting_history(self):
        self.click(LocatorsUsers.XCH_BUTTON_NEXT)

    def click_all_check_box_collection_history(self):
        self.click_on_elements(LocatorsUsers.XCH_ALL_CHECK_BOXS)

    def select_options_for_FK_SHOKS(self):
        triangles = self.page.locator(LocatorsUsers.XCH_ALL_TRIANGLES_SECOND_COLLECTION).all()
        for triangle in triangles:
            triangle.click()
            if self.expect_visible_elements(LocatorsUsers.XCH_ANSWERS_0):
                self.click(LocatorsUsers.XCH_ANSWERS_0)
            if self.expect_visible_elements(LocatorsUsers.XCH_ANSWER_BODY_POSITION_0):
                self.click(LocatorsUsers.XCH_ANSWER_BODY_POSITION_0)
            if self.expect_visible_elements(LocatorsUsers.XCH_ANSWER_LIVER_0):
                self.click(LocatorsUsers.XCH_ANSWER_LIVER_0)
            if self.expect_visible_elements(LocatorsUsers.XCH_ANSWER_LVL_SAD_0):
                self.click(LocatorsUsers.XCH_ANSWER_LVL_SAD_0)

    def calculate_FK_NYHA(self):
        self.fill_text(LocatorsUsers.XCH_INPUT_METERS, '20')
        self.click(LocatorsUsers.XCH_BUTTON_CALCULATE)

    def save_second_collecting_history(self):
        self.click(LocatorsUsers.XCH_BUTTON_NEXT)

