import pytest
from PageLocators.locators import Locators as Loc
import time
from tests.config import *


class TestPageHelp:
    elements = {Loc.PageHelp.PANEL1_HELP: Loc.PageHelp.OPEN_PANEL1_HELP,
                Loc.PageHelp.PANEL2_HELP: Loc.PageHelp.OPEN_PANEL2_HELP,
                Loc.PageHelp.PANEL3_HELP: Loc.PageHelp.OPEN_PANEL3_HELP,
                Loc.PageHelp.PANEL4_HELP: Loc.PageHelp.OPEN_PANEL4_HELP,
                Loc.PageHelp.PANEL5_HELP: Loc.PageHelp.OPEN_PANEL5_HELP,
                Loc.PageHelp.PANEL6_HELP: Loc.PageHelp.OPEN_PANEL6_HELP,
                Loc.PageHelp.PANEL7_HELP: Loc.PageHelp.OPEN_PANEL7_HELP}

    @staticmethod
    def test_bac_auth_from_help(page_help):
        page_help.click(page_help.PageHelp.BUTTON_BAC_AUTH)
        page_help.expect_visible_element(page_help.PageAuth.BUTTON_LOG)

    @staticmethod
    @pytest.mark.parametrize('panel_help, open_panel_help', [(panel_help, open_panel_help)
                                                             for panel_help, open_panel_help
                                                             in elements.items()])
    def test_open_panels_help(page_help, panel_help, open_panel_help):
        page_help.click(panel_help)
        page_help.expect_visible_element(open_panel_help)
