from dataclasses import dataclass
from typing import Dict, List

import configparser


@dataclass
class DbConfig:
    host: str
    port: int
    name: str
    user: str
    password: str
    password_hash: str


@dataclass
class ApiConfig:
    host_port: str


@dataclass
class UrlConfig:
    base: str
    users: str
    all_measurements: str
    help: str
    support: str


@dataclass
class UserCredentials:
    password_valid: str
    password_invalid: str
    admin_tele: str
    admin_amb: str
    admin_crb: str
    doctor_tele: str
    doctor_amb: str
    doctor_crb: str
    invalid_mail: str


@dataclass
class Config:
    db: DbConfig
    api: ApiConfig
    urls: UrlConfig
    creds: UserCredentials

    @property
    def admin_emails(self) -> List[str]:
        return [
            self.creds.admin_tele,
            self.creds.admin_amb,
            self.creds.admin_crb
        ]

    @property
    def doctor_emails(self) -> List[str]:
        return [
            self.creds.doctor_tele,
            self.creds.doctor_amb,
            self.creds.doctor_crb
        ]

    @property
    def email_name_mapping(self) -> Dict[str, str]:
        return {
            self.creds.admin_tele: "Админ Телемедцентра",
            self.creds.admin_amb: "Админ Скорой",
            self.creds.admin_crb: "Админ Црб",
            self.creds.doctor_tele: "Доктор Телемедцентра",
            self.creds.doctor_amb: "Доктор Скорой",
            self.creds.doctor_crb: "Доктор Црб"
        }


def load_config(path: str = "config.ini") -> Config:
    config = configparser.ConfigParser()
    config.read(path)

    return Config(
        db=DbConfig(**config["database"]),
        api=ApiConfig(**config["api"]),
        urls=UrlConfig(**config["auth_urls"]),
        creds=UserCredentials(**config["credentials"])
    )