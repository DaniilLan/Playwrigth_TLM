import random
from russian_names import RussianNames
import string

url_auth_test = 'http://1928081/'
url_users_test = 'http://181/users'
url_allm_test = 'http://192./all-measurements'
url_help_test = 'http://192:8081/help'
url_support_test = 'http://192.181/support'

list_url_test = [url_support_test, url_help_test, url_auth_test, url_users_test]

password_all = ''
invalid_pass = ''

cred = {"m": 'Админ Телемедцентра',
        "m": 'Админ Скорой',
        "dm": 'Админ Црб',
        "tc": 'Доктор Телемедцентра',
        "dom": 'Доктор Скорой',
        "tm": 'Доктор Црб',
        ".ru": 'Доктор Фап'}  # Без медработник ФАП и Пациент Фап.

mails_doc = ["u"]
mail_lan_doc = "Tdoc"
mail_lan_adm = "Te.ru"
mail_adm = "am"
mail_doc = "tdoc"
mails_adm = ["adm"]
invalid_mail = "u"
valid_mail = 'lu'


def random_phone():
    """Создание нмоера-телефона из 10 рандомных цифр без +7 (пример - 9276013854)"""
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(numbers)
    numbers_str = ''
    for i in numbers:
        numbers_str += str(i)
    return numbers_str


def random_fio(value='FIO'):
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
    """Создание рандомного mail"""
    mail = ''.join(random.choice(string.ascii_letters) for _ in range(8)) + str(random.randint(1, 1000)) + "@gmail.com"
    return mail


