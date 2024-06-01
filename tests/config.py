url_auth_test = 'http://192.168.7.221:8081/'
url_users_test = 'http://192.168.7.221:8081/users'
url_allm_test = 'http://192.168.7.221:8081/all-measurements'
url_help_test = 'http://192.168.7.221:8081/help'
url_support_test = 'http://192.168.7.221:8081/support'

list_url_test = [url_support_test, url_help_test, url_auth_test, url_users_test]
password_all = '12345678'

cred = {"adm@adm.com": 'Админ Телемедцентра',
        "spadm@adm.adm": 'Админ Скорой',
        "testadm@adm.adm": 'Админ Црб',
        "testdoc@doc.doc": 'Доктор Телемедцентра',
        "doc@doc.com": 'Доктор Скорой',
        "testdoc@doc.com": 'Доктор Црб',
        "d.s.ivanov1@samsmu.ru": 'Доктор Фап'}  # Без медработник ФАП и Пациент Фап.

mails_doc = ["testdoc@doc.doc", "doc@doc.com", "testdoc@doc.com", "d.s.ivanov1@samsmu.ru"]
mails_adm = ["adm@adm.com", "spadm@adm.adm", "testadm@adm.adm"]

access_token = ("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHAudXNlcl9pZCI6MTAxLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQu"
                "Y29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJhZG1pbiIsIm9yZy5pZCI6MTAwLCJzdWIiOiJtZWRtb24iL"
                "CJpYXQiOjE3MTcxNDUxODIuMCwiZXhwIjoxNzE3MTcwMzgyLjAsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3Q6NzIwNCIsImF1ZC"
                "I6Imh0dHA6Ly9sb2NhbGhvc3Q6NzIwNCJ9.B0ue4rE7FZxsVxbdr26DyIPQIiN7jcsbtH5FLTR6O5c")

