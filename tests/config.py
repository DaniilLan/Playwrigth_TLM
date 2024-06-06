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
mail_doc = "testdoc@doc.doc"
mail_lan = "landan2024@mail.ru"
password_lan = '123456789'
mail_adm = "adm@adm.com"
mails_adm = ["adm@adm.com", "spadm@adm.adm", "testadm@adm.adm"]


access_token = ("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHAudXNlcl9pZCI6MTAxLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQu"
                "Y29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJhZG1pbiIsIm9yZy5pZCI6MTAwLCJzdWIiOiJtZWRtb24iL"
                "CJpYXQiOjE3MTc2Nzg2NzAuMCwiZXhwIjoxNzE3NzAzODcwLjAsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3Q6NzIwNCIsImF1ZC"
                "I6Imh0dHA6Ly9sb2NhbGhvc3Q6NzIwNCJ9.Ur69rl4Akip1wcO21roZT2mezN8GFKOhwcUVUW1sZ6k")

