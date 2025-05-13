from core.db.db import DBManager

db = DBManager()

print(db.create_user(role_name='patient'))
