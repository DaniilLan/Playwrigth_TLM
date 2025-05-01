import random
from russian_names import RussianNames
import string
from PageLocators.locators import LocatorsPageHelp, LocatorsPageUsers

url_auth_test = 'http://192.168.7.221:8085/'
url_users_test = 'http://192.168.7.221:8085/users'
url_allm_test = 'http://192.168.7.221:8085/all-measurements'
url_help_test = 'http://192.168.7.221:8085/help'
url_support_test = 'http://192.168.7.221:8085/support'

list_url_test = [url_support_test, url_help_test, url_auth_test, url_users_test]

password_all = '12345678'
invalid_pass = '12345687'

cred = {"adm@tele.com": 'Админ Телемедцентра',
        "adm@amb.com": 'Админ Скорой',
        "adm@crb.com": 'Админ Црб',
        "doc@tele.com": 'Доктор Телемедцентра',
        "doc@amb.com": 'Доктор Скорой',
        "doc@crb.com": 'Доктор Црб',}

mail_adm_tele = "adm@tele.com"
mail_adm_amb = "adm@amb.com"
mail_adm_crb = "adm@crb.com"
mail_doc_tele = "doc@tele.com"
mail_doc_amb = "doc@amb.com"
mail_doc_crb = "doc@crb.com"

mails_doc = ["doc@tele.com", "doc@amb.com", "doc@crb.com"]
mails_adm = ["adm@tele.com", "adm@amb.com", "adm@crb.com"]
invalid_mail = "123123@mail.ru"

help_panels = {LocatorsPageHelp.PANEL1_HELP: LocatorsPageHelp.OPEN_PANEL1_HELP,
              LocatorsPageHelp.PANEL2_HELP: LocatorsPageHelp.OPEN_PANEL2_HELP,
              LocatorsPageHelp.PANEL3_HELP: LocatorsPageHelp.OPEN_PANEL3_HELP,
              LocatorsPageHelp.PANEL4_HELP: LocatorsPageHelp.OPEN_PANEL4_HELP,
              LocatorsPageHelp.PANEL5_HELP: LocatorsPageHelp.OPEN_PANEL5_HELP,
              LocatorsPageHelp.PANEL6_HELP: LocatorsPageHelp.OPEN_PANEL6_HELP,
              LocatorsPageHelp.PANEL7_HELP: LocatorsPageHelp.OPEN_PANEL7_HELP}

required_fields_change_profile = [LocatorsPageUsers.INPUT_CHANGE_F,
                                 LocatorsPageUsers.INPUT_CHANGE_I,
                                 LocatorsPageUsers.INPUT_CHANGE_MAIL,
                                 LocatorsPageUsers.INPUT_CHANGE_PHONE]

placeholders_required_fields_change_profile = [LocatorsPageUsers.PLACEHOLDER_CHANGE_F,
                                               LocatorsPageUsers.PLACEHOLDER_CHANGE_I,
                                               LocatorsPageUsers.PLACEHOLDER_CHANGE_MAIL,
                                               LocatorsPageUsers.PLACEHOLDER_CHANGE_PHONE]

lvl_orgs = [LocatorsPageUsers.ORG_LVL0,
            LocatorsPageUsers.ORG_LVL1,
            LocatorsPageUsers.ORG_LVL2,
            LocatorsPageUsers.ORG_LVL3]

def random_phone():
    """Создание нмоера-телефона из 10 рандомных цифр без +7 (пример - 9276013854)"""
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(numbers)
    numbers_str = ''
    for i in numbers:
        numbers_str += str(i)
    return numbers_str


def random_fio(value='I'):
    """Создание рандомого ФИО

    Указать в параметре нужное значение ФИО.

    'FIO' - верентся ФИО *По умолчанию

    'F' - вернется фамилия

    'I' - вернется имя

    'O' - вернется отчество
    """
    rn = RussianNames(count=1, name_reduction=False, patronymic_reduction=False, surname_reduction=False)
    fio = str(rn.get_batch()[0])
    if value == 'FIO':
        fio = fio.split()
        fio = fio[2]+' '+fio[0]+' '+fio[1]
        fio = str(fio)
    elif value == 'I':
        firstname = fio.split()
        fio = str(firstname[0])
    elif value == 'F':
        lastname = fio.split()
        fio = str(lastname[2])
    elif value == "O":
        patronymic = fio.split()
        fio = str(patronymic[1])
    return fio


def random_data():
    """Создание рандомной даты (пример - 03072001)"""
    month = str(random.randint(1, 12)).zfill(2)
    day = str(random.randint(1, 28)).zfill(2) if month == '02' else str(random.randint(1, 31)).zfill(2)
    year = str(random.randint(1900, 2024))
    date = day + month + year
    return date


def random_height_weight():
    """Создание рандомного числа для полей 'Рост/Вес'"""
    height_weight = str(random.randint(1, 250))
    return height_weight


def random_mail():
    """Создание рандомного mail (только строчные буквы)"""
    mail = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))  # 8 строчных букв
    mail += str(random.randint(1, 1000))  # случайное число
    mail += "@gmail.com"  # домен
    return mail

def random_name():
    """Создание рандомного name (только строчные буквы)"""
    name = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))  # 8 строчных букв
    name += str(random.randint(1, 1000))  # случайное число
    return name


