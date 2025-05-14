class LocatorsBase:
    LOGO_SAMGMU = 'img[src="/conf/logo.png"]'
    YEAR_BOT = 'div[class="copyRight__FpJl"]'
    HELP_LINK = '//a[text()="Помощь"]'
    SUPPORTS_LINK = '//a[text()="Поддержка"]'
    NOTIFICATION_ALL = '//*[@id="rootTelemedHub"]/div[1]/div'
    BUTTON_UPDATE = '//button[//text()="Обновить"]'

    base_elements = [LOGO_SAMGMU,
                     YEAR_BOT,
                     HELP_LINK,
                     SUPPORTS_LINK]