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

    BUTTON_LOGS_AUDIT = '//*[@id="rootTelemedHub"]/div[2]/main/div/div[1]/div[2]/button[1]'

    BUTTON_LOAD_PATIENT = '//*[@id="rootTelemedHub"]/div[2]/main/div/div[1]/div[2]/button[2]'

    BUTTON_ADD_USERS = '//*[@id="rootTelemedHub"]/div[2]/main/div/div[1]/div[2]/button[3]'

    BUTTON_ADD_PATIENT = '//*[@id="rootTelemedHub"]/div[2]/main/div/div[1]/div[2]/button'

