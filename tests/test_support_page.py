# class TestPageSupport(LocatorsSupport):
#
#     @staticmethod
#     def test_bac_auth_from_support(page_support):
#         page_support.click(LocatorsSupport.BUTTON_BAC_AUTH)
#         page_support.expect_visible_elements(LocatorsAuth.BUTTON_LOG)
#
#     @staticmethod
#     def test_mail_link(page_support):
#         mail_link = LocatorsSupport.LINK_PHONE
#         mail = page_support.get_attribute_element(mail_link, 'href')
#         mail_text = page_support.get_text(mail_link)
#         page_support.click(mail_link)
#         assert mail_text in mail
#
#     @staticmethod
#     def test_phone_link(page_support):
#         phone_link = LocatorsSupport.LINK_PHONE
#         phone = page_support.get_attribute_element(phone_link, 'href')
#         phone_text = page_support.get_text(phone_link)
#         page_support.click(phone_link)
#         assert phone_text in phone
