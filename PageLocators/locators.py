from Methods.methods_page import *


class LocatorsPage(MethodsPageUsers):

    NAME_PROFILE = '//*[@id="rootTelemedHub"]//div/div/div[2]/strong'

    INPUT_MAIL = '//*[@id="rootTelemedHub"]/div[2]/main/div/form/div[1]/div[1]/div/input'

    INPUT_PASSWORD = '//*[@id="rootTelemedHub"]/div[2]/main/div/form/div[1]/div[2]/div/input'

    BUTTON_LOG = '//*[@id="rootTelemedHub"]/div[2]/main/div/form/div[2]/button'

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

    FORM_FILTER = 'div[class="filterForm__PexX"]'

    INPUT_BOXS_FILTER = 'div[class="InputBox productTheme__a5bf InputBox__fca7"]'

    # FILTER_INPUT_F =
    #
    # FILTER_INPUT_I =
    #
    # FILTER_INPUT_O =
    #
    # FILTER_INPUT_DATA =
    #
    # FILTER_INPUT_GENDER =
    #
    # FILTER_INPUT_OLD_1 =
    #
    # FILTER_INPUT_OLD_2 =

    DROPDOWN_BOXS_FILTER = 'div[class="SelectMulti SelectMulti__ff0e Dropdown productTheme Dropdown__d478"]'
