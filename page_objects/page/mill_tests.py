import time
from typing import Union, List

from core.utils.file_helpers import *
from page_objects.base_page import BasePage

import re


class LocatorsMMIL:
    LINK_TEST_MMIL = '//span[text()="Методика многостороннего исследования личности (ММИЛ)"]'
    LINK_TEST_CAH = '//span[text()="Опросник «Самочувствие, Активность, Настроение» (САН)"]'
    BUTTON_NEXT_MANUAL = '//button[text()="Далее"]'
    ANSWER_YES = '//div[span[text()="Да"]]'
    ANSWER_NO = '//div[span[text()="Нет"]]'
    BUTTON_SAVE_ANSWER = '//button[text()="Сохранить"]'
    LAST_PAGE_TEST = '//span[text()="377 из 377"]'
    CAH_ANSWER_1 = '//div[@class="CPYE"]//div[span[text()="3"]]'
    NOTIFICATION = '//div[text()="Тест пройден. За результатами обратитесь к врачу."]'


class MMILPage(BasePage):

    def select_test_mmil(self):
        self.click(LocatorsMMIL.LINK_TEST_MMIL)

    def select_test_CAH(self):
        self.click(LocatorsMMIL.LINK_TEST_CAH)

    def skip_manual(self):
        self.click(LocatorsMMIL.BUTTON_NEXT_MANUAL)

    def click_answer_yes(self):
        self.click(LocatorsMMIL.ANSWER_YES)

    def click_answer_no(self):
        self.click(LocatorsMMIL.ANSWER_NO)

    def save_answer_in_test(self):
        self.click(LocatorsMMIL.BUTTON_SAVE_ANSWER)

    def answer_oly_yes_until_last_question(self):
        while not self.expect_visible_elements(LocatorsMMIL.LAST_PAGE_TEST):
            self.click_answer_yes()
            self.save_answer_in_test()

    def click_by_answer(self, class_name: str, text: str):
        locator = f'//div[@class="{class_name}"]//div[span[text()="{text}"]]'
        self.click(locator)

    def expect_notification_completed_test(self):
        self.expect_text(LocatorsMMIL.NOTIFICATION, 'Тест пройден. За результатами обратитесь к врачу.')

    def log_in_and_create_test_go_to_test_CAH(self):
        self.fill_text('//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div/input', 'testdoctor@mail.ru')
        self.fill_text('//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div/input', 'Testdoctor1!')
        self.click('//*[@id="root"]/div/div[1]/div/div[2]/button')
        self.click('//*[@id="root"]/div/div[1]/main/ul/li')
        self.click('//*[@id="root"]/div/div[1]/main/div[2]/div/button')
        self.click('//html/body/div[2]/div/div[3]/ul/div[2]')
        self.click('//html/body/div[2]/div/div[3]/div[2]/button')
        self.click('//html/body/div[2]/div/div[3]/div[2]/div/div[2]/ul[3]/div[2]/div/div')
        self.click('//html/body/div[2]/div/div[3]/div[2]/button')
        url_test = self.page.get_attribute('//html/body/div[2]/div/div[2]/div[2]/div/input', 'value')
        self.open(url_test)
        time.sleep(1)
        self.page.reload()

    def go_to_page_doctor(self):
        self.open(self.conf.urls.mmil)

    def check_interpretation_for_test(self, interpretation):
        self.click('//*[@id="root"]/div/div[1]/main/ul/li')
        self.click('//*[@id="root"]/div/div[1]/main/div[2]/table/tbody/tr[1]/td[5]/div/button[2]')
        self.click('//html/body/div[2]/div/ul/div[2]')
        time.sleep(1)
        self.click('//html/body/div[2]/div/div[4]/div/div[2]/div/span')
        time.sleep(1)
        text_inter = ''
        if interpretation == interpretation_2_31:
            text_inter = text_interpretation_2
        elif interpretation == interpretation_2_35:
            text_inter = text_interpretation_2
        elif interpretation == interpretation_2_45:
            text_inter = text_interpretation_2
        elif interpretation == interpretation_3_46:
            text_inter = text_interpretation_3
        elif interpretation == interpretation_3_50:
            text_inter = text_interpretation_3
        elif interpretation == interpretation_3_70:
            text_inter = text_interpretation_3
        elif interpretation == interpretation_3_71:
            text_inter = text_interpretation_3
        elif interpretation == interpretation_2_example:
            text_inter = text_interpretation_2
        elif interpretation == interpretation_2_120:
            text_inter = text_interpretation_2
        elif interpretation == interpretation_3_max_210:
            text_inter = text_interpretation_3
        elif interpretation == interpretation_1_min_30:
            text_inter = text_interpretation_1
        fact_text = self.get_text('//html/body/div[2]/div/div[3]/div/div[3]/div/div[2]/span')
        assert fact_text == text_inter, f'{fact_text} != {text_inter}'
