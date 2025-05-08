class LocatorsHelp:
    BUTTON_BAC_AUTH = '//span[text()="Авторизация"]'
    PANELS_HELP = (
        '//div[@class="MuiButtonBase-root MuiAccordionSummary-root MuiAccordionSummary-gutters css-1oqimao"]')
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
    help_panels = {PANEL1_HELP: OPEN_PANEL1_HELP,
                   PANEL2_HELP: OPEN_PANEL2_HELP,
                   PANEL3_HELP: OPEN_PANEL3_HELP,
                   PANEL4_HELP: OPEN_PANEL4_HELP,
                   PANEL5_HELP: OPEN_PANEL5_HELP,
                   PANEL6_HELP: OPEN_PANEL6_HELP,
                   PANEL7_HELP: OPEN_PANEL7_HELP}

