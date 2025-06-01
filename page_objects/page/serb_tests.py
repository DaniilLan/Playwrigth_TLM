import time

from core.utils.files_helpers.CAH_data import *
from core.utils.files_helpers.OKO_data import OKO
from page_objects.base_page import BasePage


class LocatorsSERB:
    LINK_TEST_MMIL = '//span[text()="Методика многостороннего исследования личности (ММИЛ)"]'
    LINK_TEST_CAH = '//span[text()="Опросник «Самочувствие, Активность, Настроение» (САН)"]'
    LINK_TEST_IIG = '//span[text()="ЭЭГ-показатели для скрининга аффективной патологии"]'
    LINK_TEST_ITRAC = '//span[text()="ОСНОВНЫЕ ПАРАМЕТРЫ, АНАЛИЗИРУЕМЫЕ В ХОДЕ ОКУЛОГРАФИЧЕСКОГО ИССЛЕДОВАНИЯ (В СИСТЕМЕ Tobii Pro Lab)"]'
    LINK_TEST_OKO = '//span[text()="Опросник когнитивных ошибок (ОКО)"]'
    LINK_TEST_BPC = '//span[text()="Показатели вариабельности ритма сердца (ВРС)"]'
    BUTTON_NEXT_MANUAL = '//button[text()="Далее"]'
    ANSWER_YES = '//div[span[text()="Да"]]'
    ANSWER_NO = '//div[span[text()="Нет"]]'
    BUTTON_SAVE_ANSWER = '//button[text()="Сохранить"]'
    LAST_PAGE_TEST = '//span[text()="377 из 377"]'
    CAH_ANSWER_1 = '//div[@class="CPYE"]//div[span[text()="3"]]'
    NOTIFICATION = '//div[text()="Тест пройден. За результатами обратитесь к врачу."]'
    PATIENT_OKO = '//li[.//span[text()="Тест ОКО "]]'
    ADD_OBSLED = '//*[@id="root"]/div/div[1]/main/div[2]/div/button'
    KLASTER_2 = '//div[span[text()="Психодиагностическое обследование"]]'
    SHARE_TEST = '//html/body/div[2]/div/div[3]/div[2]/button'
    CHAK_BOX_OKO = '//html/body/div[2]/div/div[3]/div[2]/div/div[2]/ul[1]/div[3]/div/div'
    SHARE_LINK_TEST = '//html/body/div[2]/div/div[2]/div[2]/div/input'
    BUTTON_RESULT_TEST = '//*[@id="root"]/div/div[1]/main/div[2]/table/tbody/tr[1]/td[5]/div/button[2]'
    RESULT_TEST_OKO = "//span[text()='Опросник когнитивных ошибок (ОКО)']"

class SerbPage(BasePage):

    def select_test_MMIL(self):
        self.click(LocatorsSERB.LINK_TEST_MMIL)

    def select_test_IIG(self):
        self.click(LocatorsSERB.LINK_TEST_IIG)

    def select_test_ITRAC(self):
        self.click(LocatorsSERB.LINK_TEST_ITRAC)

    def select_test_OKO(self):
        self.click(LocatorsSERB.LINK_TEST_OKO)

    def select_test_BPC(self):
        self.click(LocatorsSERB.LINK_TEST_BPC)

    def select_test_CAH(self):
        self.click(LocatorsSERB.LINK_TEST_CAH)

    def skip_manual(self):
        self.click(LocatorsSERB.BUTTON_NEXT_MANUAL)

    def click_answer_yes(self):
        self.click(LocatorsSERB.ANSWER_YES)

    def click_answer_no(self):
        self.click(LocatorsSERB.ANSWER_NO)

    def save_answer_in_test(self):
        self.click(LocatorsSERB.BUTTON_SAVE_ANSWER)

    def answer_oly_yes_until_last_question(self):
        while not self.expect_visible_elements(LocatorsSERB.LAST_PAGE_TEST):
            self.click_answer_yes()
            self.save_answer_in_test()

    def click_by_answer(self, class_name: str, text: str):
        locator = f'//div[@class="{class_name}"]//span[text()="{text}"]'
        self.click(locator)

    def expect_notification_completed_test(self):
        self.wait_visible_elements(LocatorsSERB.NOTIFICATION)
        self.expect_text(LocatorsSERB.NOTIFICATION, 'Тест пройден. За результатами обратитесь к врачу.')

    def create_test_go_to_test_CAH(self):
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

    def create_test_go_to_test_MMIL(self):
        self.click('//*[@id="root"]/div/div[1]/main/ul/li')
        self.click('//*[@id="root"]/div/div[1]/main/div[2]/div/button')
        self.click('//html/body/div[2]/div/div[3]/ul/div[2]')
        self.click('//html/body/div[2]/div/div[3]/div[2]/button')
        self.click('//html/body/div[2]/div/div[3]/div[2]/div/div[2]/ul[1]/div[1]/div/div')
        self.click('//html/body/div[2]/div/div[3]/div[2]/button')
        url_test = self.page.get_attribute('//html/body/div[2]/div/div[2]/div[2]/div/input', 'value')
        self.open(url_test)
        time.sleep(1)
        self.page.reload()

    def create_test_go_to_test_BPC(self):
        self.click('//*[@id="root"]/div/div[1]/main/ul/li')
        self.click('//*[@id="root"]/div/div[1]/main/div[2]/div/button')
        self.click('//html/body/div[2]/div/div[3]/ul/div[3]')
        self.click('//html/body/div[2]/div/div[3]/div[2]/div/div[2]/ul/div[2]/div/div')
        self.click('//html/body/div[2]/div/div[3]/div[2]/button')
        url_test = self.page.get_attribute('//html/body/div[2]/div/div[2]/div[2]/div/input', 'value')
        self.open(url_test)
        time.sleep(1)
        self.page.reload()

    def create_test_go_to_test_IIG(self):
        self.click('//*[@id="root"]/div/div[1]/main/ul/li')
        self.click('//*[@id="root"]/div/div[1]/main/div[2]/div/button')
        self.click('//html/body/div[2]/div/div[3]/ul/div[3]')
        self.click('//html/body/div[2]/div/div[3]/div[2]/div/div[2]/ul/div[3]/div/div')
        self.click('//html/body/div[2]/div/div[3]/div[2]/button')
        url_test = self.page.get_attribute('//html/body/div[2]/div/div[2]/div[2]/div/input', 'value')
        self.open(url_test)
        time.sleep(1)
        self.page.reload()

    def create_test_go_to_test_ITREC(self):
        self.click('//*[@id="root"]/div/div[1]/main/ul/li')
        self.click('//*[@id="root"]/div/div[1]/main/div[2]/div/button')
        self.click('//html/body/div[2]/div/div[3]/ul/div[3]')
        self.click('//html/body/div[2]/div/div[3]/div[2]/div/div[2]/ul/div[1]/div/div')
        self.click('//html/body/div[2]/div/div[3]/div[2]/button')
        url_test = self.page.get_attribute('//html/body/div[2]/div/div[2]/div[2]/div/input', 'value')
        self.open(url_test)
        time.sleep(1)
        self.page.reload()

    def create_test_go_to_test_OKO(self):
        self.click(LocatorsSERB.PATIENT_OKO)
        self.click(LocatorsSERB.ADD_OBSLED)
        self.click(LocatorsSERB.KLASTER_2)
        self.click(LocatorsSERB.SHARE_TEST)
        self.click(LocatorsSERB.CHAK_BOX_OKO)
        self.click(LocatorsSERB.SHARE_TEST)
        url_test = self.page.get_attribute(LocatorsSERB.SHARE_LINK_TEST, 'value')
        self.open(url_test)
        time.sleep(1)
        self.page.reload()

    def go_to_page_doctor(self):
        self.open(self.conf.urls.mmil)

    def check_interpretation_for_test_CAN(self, answer):
        self.click('//*[@id="root"]/div/div[1]/main/ul/li')
        self.click('//*[@id="root"]/div/div[1]/main/div[2]/table/tbody/tr[1]/td[5]/div/button[2]')
        self.click('//html/body/div[2]/div/ul/div[2]')
        time.sleep(1)
        self.click('//html/body/div[2]/div/div[4]/div/div[2]/div/span')
        time.sleep(1)
        text_inter = ''
        if answer is CAH.answers_1_34:
            text_inter = CAH.text_interpretation_1
        elif answer is CAH.answers_1_60:
            text_inter = CAH.text_interpretation_1
        elif answer is CAH.answers_1_90:
            text_inter = CAH.text_interpretation_1
        elif answer is CAH.answers_2_99:
            text_inter = CAH.text_interpretation_1
        elif answer == CAH.answers_1_96:
            text_inter = CAH.text_answer_1
        elif answer == CAH.answers_2_102:
            text_inter = CAH.text_answer_2
        elif answer == CAH.answers_2_105:
            text_inter = CAH.text_answer_2
        elif answer == CAH.answers_2_120:
            text_inter = CAH.text_answer_2
        elif answer == CAH.answers_2_135:
            text_inter = CAH.text_answer_2
        elif answer == CAH.answers_2_138:
            text_inter = CAH.text_answer_2
        elif answer == CAH.answers_3_144:
            text_inter = CAH.text_answer_3
        elif answer == CAH.answers_3_150:
            text_inter = CAH.text_answer_3
        elif answer == CAH.answers_2_example:
            text_inter = CAH.text_answer_2
        elif answer == CAH.answers_2_120:
            text_inter = CAH.text_answer_2
        elif answer == CAH.answers_3_max_210:
            text_inter = CAH.text_answer_3
        elif answer == CAH.answers_1_min_30:
            text_inter = CAH.text_answer_1
        fact_text = self.get_text('//html/body/div[2]/div/div[3]/div/div[3]/div/div[2]/span')
        assert fact_text == text_inter, (f'{fact_text} \n'
                                         f'!= {text_inter}\n'
                                         f'protokolId: \n'
                                         f'testId: \n')

    def delete_all_obs(self, FIO):
        self.click(f'//span[text()="{FIO}"]')
        button_delete = '//div[@class="passedTests-delete"]'
        while self.wait_visible_elements(button_delete):
            self.click(button_delete)
            self.click('//button[@class="button warning fullwidth"]')

    def fill_all_input_fields_IIG(self):
        text = '11111111'
        for i in range(4):
            self.fill_text(f'//*[@id="popap_window"]/div/div/div/div[2]/div[3]/div/div/div[2]/div[{i+5}]/input', text)
        for k in range(20):
            self.fill_text(f'//*[@id="popap_window"]/div/div/div/div[2]/div[3]/div/div/div[2]/div[{k+11}]/input', text)

    def fill_all_input_fields_ITRAC(self):
        text = '11111111'
        for i in range(4):
            self.fill_text(f'//*[@id="popap_window"]/div/div/div/div[2]/div[3]/div/div/div[2]/div[{i+5}]/input', text)
        for k in range(8):
            self.fill_text(f'//*[@id="popap_window"]/div/div/div/div[2]/div[3]/div/div/div[2]/div[{k+11}]/input', text)

    def fill_all_input_fields_BPC(self):
        text = '11111111'
        for i in range(4):
            self.fill_text(f'//*[@id="popap_window"]/div/div/div/div[2]/div[3]/div/div/div[2]/div[{i+5}]/input', text)
        for k in range(20):
            self.fill_text(f'//*[@id="popap_window"]/div/div/div/div[2]/div[3]/div/div/div[2]/div[11]/div[2]/div[{k+1}]/input', text)
        for j in range(20):
            self.fill_text(f'//*[@id="popap_window"]/div/div/div/div[2]/div[3]/div/div/div[2]/div[12]/div[2]/div[{j+1}]/input', text)
        for e in range(3):
            self.fill_text(f'//*[@id="popap_window"]/div/div/div/div[2]/div[3]/div/div/div[2]/div[13]/div[2]/div[{e+1}]/input', text)

    def check_interpretation_for_test_OKO(self, answer):
        self.click(LocatorsSERB.PATIENT_OKO)
        self.click(LocatorsSERB.BUTTON_RESULT_TEST)
        self.click(LocatorsSERB.KLASTER_2)
        time.sleep(1)
        self.click(LocatorsSERB.RESULT_TEST_OKO)
        time.sleep(1)
        if answer is OKO.answer_all_limit or OKO.answer_all_max:
            for kay in OKO.interpretations: # Я убрал тут items() так как мне нужно доставить только ключи "kay" из словаря интерпретаций
                scale, true_interpretations = OKO.interpretations[kay]
                text_inter = self.get_text(f'//div[@class="testConclusion-container"][.//span[text()="{scale}"]]')
                assert text_inter == true_interpretations, (f"Ошибка текст "
                                                            f"\nФР: {text_inter} "
                                                            f"\n!= "
                                                            f"\nОР: {true_interpretations}")
        # Нужно написать условие, которые будет проверять отсутствие шкал (интерпретаций)
        # Для данной реализации можно воспользоваться примером цикла выше, взяв от туда сам цикл и сроку для получения текста.
        # Изменив метод получения текста по локатору на метод, который проверяет "не" видимость элемента - получим ожидаемую реализацию.
        # Метод для "не" видимости элемента:
        # element = page.locator("XPath-какой-то")
        # expect(element).not_to_be_visible()