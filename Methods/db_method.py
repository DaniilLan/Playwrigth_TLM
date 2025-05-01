import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os
from tests.config import *

load_dotenv()


class QueryDB:
    def __init__(self):
        self.connection_params = {
            'host': os.getenv('DB_HOST'),
            'port': os.getenv('DB_PORT'),
            'dbname': os.getenv('DB_NAME'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'application_name': "API-test"
        }

    def _get_connection(self):
        return psycopg2.connect(**self.connection_params)

    def query_create_user(
            self,
            username= random_name(),
            email= random_mail(),
            first_name="Авто",
            middle_name="Тестович",
            last_name="",
            password_hash="$argon2id$v=19$m=4096,t=3,p=3$NA1AsABbbIslp2gkSK8XG0P5IcYZ8G/Xu/tNBjfRz7o$W+u0OCso3uqyusDwX00odYPhPtaIoxP0O5QuRKMP+Bw",
            role_name="doctor"):
        conn = None
        cursor = None
        try:
            conn = self._get_connection()
            cursor = conn.cursor()

            query = """
            INSERT INTO public.users (
                created, username, email, org_id,
                first_name, middle_name, sex,
                status, password_hash, role_name,
                deleted, urgent_inspection
            ) VALUES (
                NOW(), %s, %s, 0,
                %s, %s, 'male',
                'active', %s, %s,
                FALSE, FALSE
            ) RETURNING id;
            """

            cursor.execute(query, (
                username, email,
                first_name, middle_name,
                password_hash, role_name
            ))

            user_id = cursor.fetchone()[0]
            conn.commit()

            data_user = {
                "id": user_id,
                "mail": email,
                "password": "12345678",
            }
            return data_user

        except psycopg2.Error as e:
            print(f"Ошибка при создании пользователя: {e}")
            if conn:
                conn.rollback()
            return None
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def query_delete_user(self, id_user):
        conn = self._get_connection()
        cursor = None
        try:
            cursor = conn.cursor()
            # Выполнение запроса
            if id_user:
                cursor.execute(f"DELETE FROM public.users WHERE id={id_user};")
            else:
                print("Ошибка: id_user не указан для запроса удаления лимитов и самого пользователя")

            conn.commit()
            return None

        except psycopg2.Error as e:
            print("Ошибка при выполнении запроса:", e)
            return None
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()

    def query_delete_limit(self, id_user):
        conn = self._get_connection()
        cursor = None
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            # Выполнение запроса
            if id_user:
                cursor.execute(f"DELETE FROM public.measurements_limits WHERE patient_id={id_user};")
            else:
                print("Ошибка: id_user не указан для запроса удаления лимитов")

            conn.commit()
            return None

        except psycopg2.Error as e:
            print("Ошибка при выполнении запроса:", e)
            return None
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()

    def query_delete_org(self, id_org):
        conn = self._get_connection()
        cursor = None
        try:
            cursor = conn.cursor()
            # Выполнение запроса
            if id_org:
                cursor.execute(f"DELETE FROM public.organizations WHERE id={id_org};")
            else:
                print("Ошибка: id_org не указан для запроса удаления организации")

            conn.commit()
            return None

        except psycopg2.Error as e:
            print("Ошибка при выполнении запроса:", e)
            return None
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()

    def query_delete_meeting(self, meeting_id):
        conn = self._get_connection()
        cursor = None
        try:
            cursor = conn.cursor()
            # Выполнение запроса
            if meeting_id:
                cursor.execute(f"DELETE FROM vks.meetings WHERE id={meeting_id};")
            else:
                print("Ошибка: initiator_id не указан для запроса удаления митинга")

            conn.commit()
            return None

        except psycopg2.Error as e:
            print("Ошибка при выполнении запроса:", e)
            return None
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()

    def query_delete_notification(self, recipient_id):
        conn = self._get_connection()
        cursor = None
        try:
            cursor = conn.cursor()
            # Выполнение запроса
            if recipient_id:
                cursor.execute(f"DELETE FROM public.notifications WHERE  recipient_id={recipient_id};")
            else:
                print("Ошибка: recipient_id не указан для запроса удаления уведомления")

            conn.commit()
            return None

        except psycopg2.Error as e:
            print("Ошибка при выполнении запроса:", e)
            return None
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()


# db = QueryDB()
