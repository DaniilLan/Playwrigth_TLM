from Methods.methods_page import *


class Locators(MethodsPageUsers):

    LOGO_SAMGMU = 'img[src="/conf/logo.png"]'

    YEAR_BOT = 'div[class="copyRight__FpJl"]'

    HELP_LINK = '//a[text()="Помощь"]'

    SUPPORTS_LINK = '//a[text()="Поддержка"]'

    class PageAuth:

        INPUT_MAIL = '//*[@id="rootTelemedHub"]/div[2]/main/div/form/div[1]/div[1]/div/input'

        INPUT_PASSWORD = '//*[@id="rootTelemedHub"]/div[2]/main/div/form/div[1]/div[2]/div/input'

        BUTTON_LOG = '//*[@id="rootTelemedHub"]/div[2]/main/div/form/div[2]/button'

        PLACEHOLDER_PASSWORD = '//label[text()="Пароль"]'

        PLACEHOLDER_EMAIL = '//label[text()="E-mail"]'

        LINK_FORGOT_PASSWORD = 'span[data-locator="forgotPassword"]'

        EYE_PASSWORD = 'svg[xmlns="http://www.w3.org/2000/svg"]'

        BUTTON_FORGOT = '//button[span[text()="Сбросить"]]'

        NOTIFICATION_FORGOT_PASSWORD = '//*[@id="rootTelemedHub"]/div[1]/div'

        BUTTON_CANCEL = '//span[text()="Отмена"]'

        DIV_INPUT_EMAIL = '//*[@id="rootTelemedHub"]/div[2]/main/div/form/div[1]/div[1]'

        DIV_INPUT_PASS = '//*[@id="rootTelemedHub"]/div[2]/main/div/form/div[1]/div[2]'

    class PageSupport:

        BUTTON_BAC_AUTH = '//span[text()="Авторизация"]'

        LINK_MAIL = 'a[href="mailto:help-iir@samsmu.ru"]'

        LINK_PHONE = 'a[href="tel:+7 (846) 215 11 63"]'

    class PageHelp:

        BUTTON_BAC_AUTH = '//span[text()="Авторизация"]'

        PANELS_HELP = ('//div[@class="MuiButtonBase-root MuiAccordionSummary-root '
                       'MuiAccordionSummary-gutters css-1oqimao"]')
        OPEN_PANELS_HELP = '//div[@class="MuiAccordionDetails-root css-u7qq7e"]'

        PANEL1_HELP = '//div[@id="panel1a-header"]'
        PANEL2_HELP = '//div[@id="panel2a-header"]'
        PANEL3_HELP = '//div[@id="panel3a-header"]'
        PANEL4_HELP = '//div[@id="panel4a-header"]'
        PANEL5_HELP = '//div[div[strong[text()="Настройка профиля"]]]'
        PANEL6_HELP = '//div[div[strong[text()="Порядок работы администратора в веб-приложении"]]]'
        PANEL7_HELP = '//div[div[strong[text()="Порядок работы врача в веб-приложении"]]]'

        OPEN_PANEL1_HELP = '//div[@id="panel1a-content"]'
        OPEN_PANEL2_HELP = '//div[@id="panel2a-content"]'
        OPEN_PANEL3_HELP = '//div[@id="panel3a-content"]'
        OPEN_PANEL4_HELP = '//div[@id="panel4a-content"]'
        OPEN_PANEL5_HELP = '//div[div[p[strong[text()="Изменить профиль."]]]]'
        OPEN_PANEL6_HELP = '//div[h3[text()="Регистрация пользователя"]]'
        OPEN_PANEL7_HELP = '//div[h3[text()="Регистрация пациента"]]'

    class PageUsers:

        WINDOW = '/html/body/div[2]/div/div[2]/form/div[2]/button'

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

        BUTTON_SAVE_NEW_PASS = '//html/body/div[2]/div/div[2]/form/div[5]/button[2]'

        NOTIFICAL_CHANGE_PASS = '//*[@id="rootTelemedHub"]/div[1]/div'

        BUTTON_HEADER_USERS = "a[data-locator='/users']"

        BUTTON_HEADER_ALLMS = "a[data-locator='/all-measurements']"

        BUTTON_HEADER_MEETING = "a[data-locator='/meetings']"

        BUTTON_HEADER_ORGANIZATION = "a[data-locator='/organizations']"

        BUTTON_HEADER_SETTINGS = "a[data-locator='/settings']"

        BUTTON_LOGS_AUDIT = '//div[2]/main/div/div[1]/div[2]/button[1]'

        BUTTON_LOAD_PATIENT = '//div[2]/main/div/div[1]/div[2]/button[2]'

        BUTTON_ADD_USERS = '//div[2]/main/div/div[1]/div[2]/button[3]'

        BUTTON_ADD_PATIENT = '//div[2]/main/div/div[1]/div[2]/button'

        USERS_OR_PATIENTS = "//div[2]/main/div/div[1]/div[1]"

        QUANTITY_USERS_HEADER = "//div[2]/main/div/div[1]/div[1]/span"

        QUANTITY_USERS_PAGINATION = "//div[2]/main/div/div[2]/div[2]/div[3]/div[3]"

        DROPDOWN_FILTER = '//div[2]/main/div/div[2]/div[1]/label'

        BUTTON_APPLY_FILTER = 'button[data-locator="apply"]'

        FILTER_FORM = 'div[class="filterForm__PexX"]'

        FILTER_INPUT_BOXS = '//div/div/input'

        # FILTER_INPUT_F =
        #
        # FILTER_INPUT_I =
        #
        # FILTER_INPUT_O =
        #
        # FILTER_INPUT_DATA =

        FILTER_DROPDOWN_GENDER = 'div[class="selectContainer selectContainer__e7c6"]'

        # FILTER_INPUT_OLD_1 =
        #
        # FILTER_INPUT_OLD_2 =

        FILTER_DROPDOWN_ROLE = '//div[2]/main/div/div[2]/div[1]/div/div/div/div[7]/div/div/div'

        FILTER_DROPDOWN_ORGANIZATION = '//div[@class="HeaderTitle HeaderTitle__a637"]/div[@data-locator="multiSelectInput"]'

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

        INPUT_CHANGE_PHONE = '//html/body/div[2]/div/div[2]/form/div[5]/div/div/div/input'

        PLACEHOLDER_CHANGE_F = '//div[@data-locator="lastName"]/div/label[text()="Фамилия"]'

        PLACEHOLDER_CHANGE_I = '//div[@data-locator="firstName"]/div/div/label[text()="Имя"]'

        PLACEHOLDER_CHANGE_O = '//div[@data-locator="middleName"]/div/div/label[text()="Отчество"]'

        PLACEHOLDER_CHANGE_MAIL = '//div[@data-locator="email"]/div/div/label[text()="E-mail"]'

        PLACEHOLDER_CHANGE_PHONE = '//div[@data-locator="phone"]/div/div/label[text()="Телефон"]'

        BUTTON_SAVE_PROFILE = '//body/div[2]/div/div[2]/form/div[7]/button[2]'

        BUTTON_CLOSE_CHANGE_PROFILE = '//body/div[3]/div/div[2]/form/div[7]/button[1]'

    class PageAllMeasurements:

        REPORTS = '//*[@id="rootTelemedHub"]/div[2]/main/div/div/div[1]/div[2]/div/div/div/button'

        TEXT_ALL_MEASUREMENTS = '//div/div[text()="Все измерения"]'

    class PageMeetings:

        BUTTON_ADD_MEETING = '//button[span[text()="Добавить встречу"]]'
