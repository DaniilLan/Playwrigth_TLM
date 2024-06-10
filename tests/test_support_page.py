from tests.config import *
import time
import pytest
import json
from playwright.sync_api import Route
from PageLocators.locators import Locators as Loc
import re


class TestPageSupport:

    @staticmethod
    def test_bac_auth_from_support(page_support):
        page_support.click(page_support.PageSupport.BUTTON_BAC_AUTH)
        page_support.expect_visible_element(page_support.PageAuth.BUTTON_LOG)

    @staticmethod
    def test_mail_link(page_support):
        mail_link = page_support.PageSupport.LINK_PHONE
        mail = page_support.get_attribute_element(mail_link, 'href')
        mail_text = page_support.get_text(mail_link)
        page_support.click(mail_link)
        assert mail_text in mail

    @staticmethod
    def test_phone_link(page_support):
        phone_link = page_support.PageSupport.LINK_PHONE
        phone = page_support.get_attribute_element(phone_link, 'href')
        phone_text = page_support.get_text(phone_link)
        page_support.click(phone_link)
        assert phone_text in phone
