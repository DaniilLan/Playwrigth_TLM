from Methods.methods_page import *


class Locators(MethodsPageUsers):

    LOGO_SAMGMU = 'img[src="/conf/logo.png"]'

    YEAR_BOT = 'div[class="copyRight__FpJl"]'

    FORGOT_PASSWORD = 'span[data-locator="forgotPassword"]'

    EYE = 'svg[xmlns="http://www.w3.org/2000/svg"]'

    HELP_LINK = '//a[text()="Помощь"]'

    SUPPORTS_LINK = '//a[text()="Поддержка"]'

    class PageAuth:
        INPUT_MAIL = '//*[@id="rootTelemedHub"]/div[2]/main/div/form/div[1]/div[1]/div/input'

        INPUT_PASSWORD = '//*[@id="rootTelemedHub"]/div[2]/main/div/form/div[1]/div[2]/div/input'

        BUTTON_LOG = '//*[@id="rootTelemedHub"]/div[2]/main/div/form/div[2]/button'

        PLACEHOLDER_PASSWORD = '//label[text()="Пароль"]'

        PLACEHOLDER_EMAIL = '//label[text()="E-mail"]'

        FORGOT_PASSWORD = 'span[data-locator="forgotPassword"]'

    class PageUsers:

        WINDOW = '/html/body/div[2]/div/div[2]/form/div[2]/button'

        NAME_PROFILE = '//*[@id="rootTelemedHub"]//div/div/div[2]/strong'

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

    class PageAllMeasurements:

        REPORTS = '//*[@id="rootTelemedHub"]/div[2]/main/div/div/div[1]/div[2]/div/div/div/button'

