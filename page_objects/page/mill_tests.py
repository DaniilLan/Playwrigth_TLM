import time
from typing import Union, List
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

    def wait_visible_notification(self):
        self.wait_visible_elements(LocatorsMMIL.NOTIFICATION)

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

