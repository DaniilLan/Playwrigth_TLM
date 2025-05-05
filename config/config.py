from dataclasses import dataclass

import json
import configparser

@dataclass
class CSSParams:
    error_background_color: str
    error_border_color: str


@dataclass
class PageContext:
    viewport_fhd: dict
    viewport_2k: dict


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
    css: CSSParams
    urls: UrlConfig
    context: PageContext
    creds: UserCredentials

    @property
    def admin_emails(self) -> list[str]:
        return [
            self.creds.admin_tele,
            self.creds.admin_amb,
            self.creds.admin_crb
        ]

    @property
    def doctor_emails(self) -> list[str]:
        return [
            self.creds.doctor_tele,
            self.creds.doctor_amb,
            self.creds.doctor_crb
        ]

    @property
    def email_name_mapping(self) -> dict[str, str]:
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

    viewport_fhd = json.loads(config["context_page"]["viewport_fhd"])
    viewport_2k = json.loads(config["context_page"]["viewport_2k"])

    return Config(
        db=DbConfig(**config["database"]),
        api=ApiConfig(**config["api"]),
        css=CSSParams(**config["css_params"]),
        urls=UrlConfig(**config["urls_page"]),
        creds=UserCredentials(**config["credentials"]),
        context=PageContext(
            viewport_fhd=viewport_fhd,
            viewport_2k=viewport_2k,
        ),
    )
