url_auth_test = 'http://192.168.7.221:8081/'
url_users_test = 'http://192.168.7.221:8081/users'
url_allm_test = 'http://192.168.7.221:8081/all-measurements'
url_help_test = 'http://192.168.7.221:8081/help'
url_support_test = 'http://192.168.7.221:8081/support'

list_url_test = [url_support_test, url_help_test, url_auth_test, url_users_test]

password_all = '12345678'
invalid_pass = '12345687'

cred = {"adm@adm.com": 'Админ Телемедцентра',
        "spadm@adm.adm": 'Админ Скорой',
        "testadm@adm.adm": 'Админ Црб',
        "testdoc@doc.doc": 'Доктор Телемедцентра',
        "doc@doc.com": 'Доктор Скорой',
        "testdoc@doc.com": 'Доктор Црб',
        "d.s.ivanov1@samsmu.ru": 'Доктор Фап'}  # Без медработник ФАП и Пациент Фап.

mails_doc = ["testdoc@doc.doc", "doc@doc.com", "testdoc@doc.com", "d.s.ivanov1@samsmu.ru"]
mail_lan_doc = "TestLanDoc@doc.doc"
mail_lan_adm = "TestLanAdm@mail.ru"
mail_adm = "adm@adm.com"
mail_doc = "testdoc@doc.doc"
mails_adm = ["adm@adm.com", "spadm@adm.adm", "testadm@adm.adm"]
invalid_mail = "123123@mail.ru"
valid_mail = 'landan2001@mail.ru'



