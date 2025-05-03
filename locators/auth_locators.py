class LocatorsAuth:
    INPUT_MAIL = '//*[@id="rootTelemedHub"]/div[2]/main/div/form/div[1]/div[1]/div/input'
    INPUT_PASSWORD = '//*[@id="rootTelemedHub"]/div[2]/main/div/form/div[1]/div[2]/div/input'
    BUTTON_LOG = '//*[@id="rootTelemedHub"]/div[2]/main/div/form/div[2]/button'
    PLACEHOLDER_PASSWORD = '//label[text()="Пароль"]'
    PLACEHOLDER_EMAIL = '//label[text()="Email"]'
    LINK_FORGOT_PASSWORD = 'span[data-locator="forgotPassword"]'
    EYE_PASSWORD = 'svg[xmlns="http://www.w3.org/2000/svg"]'
    BUTTON_FORGOT = '//button[span[text()="Сбросить"]]'
    BUTTON_CANCEL = '//span[text()="Отмена"]'
    DIV_INPUT_EMAIL = '//*[@id="rootTelemedHub"]/div[2]/main/div/form/div[1]/div[1]'
    DIV_INPUT_PASS = '//*[@id="rootTelemedHub"]/div[2]/main/div/form/div[1]/div[2]'

    auth_elements = [INPUT_MAIL,
                     INPUT_PASSWORD,
                     BUTTON_LOG,
                     LINK_FORGOT_PASSWORD,
                     EYE_PASSWORD,
                     PLACEHOLDER_EMAIL,
                     PLACEHOLDER_PASSWORD]
