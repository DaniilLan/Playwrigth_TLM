from contextlib import contextmanager
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, scoped_session
from core.db.models.user import User
from config.config import load_config
from core.utils.data_generators import random_name
from datetime import datetime
import logging


logger = logging.getLogger(__name__)

class DBManager:
    def __init__(self, config_path: str = "config.ini"):
        self.config = load_config(config_path)

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

    def create_user(self, role_name="doctor", **kwargs):
        """Создает тестового пользователя с минимальными обязательными полями"""
        user_data = {
            "username": random_name(),
            "org_id": 0,
            "first_name": "Тест",
            "last_name": "Тестов",
            "sex": "male",
            "birthdate": datetime.now().date(),
            "height": 180,
            "status": "active",
            "password_hash": self.config.db.password_hash,
            "role_name": role_name,
            "deleted": False,
            "urgent_inspection": False,
            **kwargs
        }

        with self.session() as s:
            user = User(**user_data)
            s.add(user)
            s.flush()
            return {
                "id": user.id,
                "username": user.username,
                "password": "12345678",
                "role_name": user.role_name
            }

    def delete_user(self, user_id):
        with self.session() as s:
            if user := s.get(User, user_id):
                s.delete(user)
            else:
                logger.warning(f"User {user_id} not found")