from os import environ
from typing import Dict, List
from pydantic import BaseModel, Field

import configparser
import json

class NamePDFDoc(BaseModel):
    user_manual: str

class TextError(BaseModel):
    invalid_mail: str
    invalid_password: str

class CSSParams(BaseModel):
    error_background_color:  str
    error_border_color: str


class PageContext(BaseModel):
    viewport_fhd: Dict[str, int]
    viewport_2k: Dict[str, int]


class DbConfig(BaseModel):
    host: str
    port: int
    name: str
    user: str
    password: str = Field(default_factory=lambda: environ.get("DB_PASSWORD"))
    password_hash: str = Field(default_factory=lambda: environ.get("DB_PASSWORD_HASH"))


class ApiConfig(BaseModel):
    host_port: str


class UrlConfig(BaseModel):
    base: str

    @property
    def users(self) -> str:
        return f"{self.base}users"

    @property
    def all_measurements(self) -> str:
        return f"{self.base}all_measurements"

    @property
    def help(self) -> str:
        return f"{self.base}help"

    @property
    def support(self) -> str:
        return f"{self.base}support"


class UserCredentials(BaseModel):
    password_valid: str
    password_invalid: str
    admin_tele: str
    admin_amb: str
    admin_crb: str
    doctor_tele: str
    doctor_amb: str
    doctor_crb: str
    invalid_mail: str


class Config(BaseModel):
    db: DbConfig
    api: ApiConfig
    css: CSSParams
    pdf: NamePDFDoc
    urls: UrlConfig
    error: TextError
    context: PageContext
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
            self.creds.admin_tele: "Докторов Админ Телемедцентра",
            self.creds.admin_amb: "Админ Скорой",
            self.creds.admin_crb: "Админ Црб",
            self.creds.doctor_tele: "Тестовый Доктор Телемедцентра",
            self.creds.doctor_amb: "Доктор Скорой",
            self.creds.doctor_crb: "Доктор Црб",
        }


def load_config(path: str = "C:/Users/dlancov/PycharmProjects/Playwrigth_TLM/config.ini") -> Config:
    config = configparser.ConfigParser()
    with open(path, 'r', encoding='utf-8') as f:
        config.read_file(f)

    viewport_fhd = json.loads(config["context_page"]["viewport_fhd"])
    viewport_2k = json.loads(config["context_page"]["viewport_2k"])

    return Config(
        db=DbConfig(**config["database"]),
        api=ApiConfig(**config["api"]),
        css=CSSParams(**config["css_params"]),
        pdf=NamePDFDoc(**config["url_pdf_doc"]),
        urls=UrlConfig(**config["urls_page"]),
        creds=UserCredentials(**config["credentials"]),
        error=TextError(**config["text_error"]),
        context=PageContext(
            viewport_fhd=viewport_fhd,
            viewport_2k=viewport_2k,
        ),
    )