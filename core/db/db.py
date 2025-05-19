from contextlib import contextmanager
from sqlalchemy import create_engine, URL, inspect, text
from sqlalchemy.orm import sessionmaker, scoped_session
from core.db.models.public import User
from config.config import load_config
from core.utils.data_generators import *
from datetime import datetime

import logging


logger = logging.getLogger(__name__)


class DBManager:
    def __init__(self):
        self.config = load_config()

        db_url = URL.create(
            drivername="postgresql",
            username=self.config.db.user,
            password=self.config.db.password,
            host=self.config.db.host,
            port=self.config.db.port,
            database=self.config.db.name
        )
        self.engine = create_engine(db_url)
        self.Session = scoped_session(sessionmaker(bind=self.engine))

    @contextmanager
    def session(self):
        session = self.Session()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            logger.error(f"DB error: {e}")
            raise
        finally:
            session.close()

    def create_user(self, role_name: str = "doctor", org_id: int = 1, **kwargs) -> dict:
        """Создает пользователя с валидными значениями по умолчанию."""
        user_data = {
            "created": datetime.now(),
            "username": random_name(),
            "org_id": org_id,  # Или явно создайте организацию
            "first_name": "АвтоТест",
            "last_name": "АвтоТестов",
            "sex": "male",
            "birthdate": datetime.now(),  # DateTime вместо date
            "height": 180,
            "status": "active",
            "password_hash": self.config.db.password_hash,
            "role_name": role_name,
            "deleted": False,
            "urgent_inspection": False,
            "email": f"{random_mail()}",  # Обязательно, если нет DEFAULT
            "phone": f"+7{random_phone()}",  # Обязательно, если нет DEFAULT
            **kwargs
        }

        with self.session() as s:
            user = User(**user_data)
            s.add(user)
            s.flush()
            return {
                "id": user.id,
                "username": user.username,
                "password": "12345678",  # Пароль должен совпадать с password_hash
                "role_name": user.role_name
            }

    from sqlalchemy import text  # Добавьте этот импорт

    def delete_user(self, user_id):
        with self.session() as s:
            try:
                # 1. Проверяем существование пользователя
                if not (user := s.get(User, user_id)):
                    logger.warning(f"User {user_id} not found")
                    return False

                # 2. Получаем метаданные БД для автоматического определения связей
                inspector = inspect(s.bind)

                # 3. Находим все таблицы, ссылающиеся на users.id
                related_tables = set()
                for table_name in inspector.get_table_names():
                    for fk in inspector.get_foreign_keys(table_name):
                        if fk['referred_table'] == 'users' and 'id' in fk['referred_columns']:
                            related_tables.add((table_name, fk['constrained_columns'][0]))

                # 4. Удаляем записи из связанных таблиц
                for table, column in related_tables:
                    try:
                        # Оберните SQL-запрос в text()
                        stmt = text(f"DELETE FROM {table} WHERE {column} = :user_id")
                        s.execute(stmt, {'user_id': user_id})
                        logger.debug(f"Deleted from {table} for user {user_id}")
                    except Exception as e:
                        logger.error(f"Error deleting from {table}: {str(e)}")
                        s.rollback()
                        return False

                # 5. Удаляем самого пользователя
                s.delete(user)
                s.commit()
                logger.info(f"Successfully deleted user {user_id}")
                return True

            except Exception as e:
                s.rollback()
                logger.error(f"Error deleting user {user_id}: {str(e)}")
                return False

