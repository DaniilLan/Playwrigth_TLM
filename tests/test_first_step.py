from locators.base_locators import LocatorsBase
from locators.auth_locators import LocatorsAuth
from locators.user_locators import LocatorsUsers
from page_objects.base_page import BasePage
import re
from config.config import load_config

import pytest


@pytest.mark.usefixtures("page")
class TestPageAuth:
    page: BasePage

    # def test_name_profile(self, conf):
    #     self.page.fill_text(LocatorsAuth.INPUT_MAIL, "doc@tele.com")
    #     self.page.fill_text(LocatorsAuth.INPUT_PASSWORD, conf.creds.password_valid)
    #     self.page.click(LocatorsAuth.BUTTON_LOG)
    #     profile = LocatorsUsers.NAME_PROFILE
    #     self.page.wait_visible_elements(profile)
    #     self.page.expect_text(profile, "Доктор Телемедц")