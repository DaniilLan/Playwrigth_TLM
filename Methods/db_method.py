import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

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
