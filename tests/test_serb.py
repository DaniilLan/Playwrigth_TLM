import time

import pytest
from core.utils.files_helpers.CAH_data import CAH
from core.utils.files_helpers.MMIL_data import MMIL
from core.utils.files_helpers.OKO_data import OKO


class TestSerb:
    # @pytest.mark.parametrize('answer', [
    #                                             CAH.answers_1_34,
    #                                             CAH.answers_1_60,
    #                                             CAH.answers_1_90,
    #                                             CAH.answers_1_96,
    #                                             CAH.answers_2_102,
    #                                             CAH.answers_2_105,
    #                                             CAH.answers_2_120,
    #                                             CAH.answers_2_135,
    #                                             CAH.answers_2_138,
    #                                             CAH.answers_3_144,
    #                                             CAH.answers_3_150,
    #                                             CAH.answers_2_example,
    #                                             CAH.answers_3_max_210,
    #                                             CAH.answers_1_min_30,
    #                                             ],
    #                          ids=[
    #                              "answers_1_34",
    #                              "answers_1_60",
    #                              "answers_1_90",
    #                              "answers_2_102",
    #                              "answers_2_105",
    #                              "answers_2_120",
    #                              "answers_2_135",
    #                              "answers_2_138",
    #                              "answers_3_144",
    #                              "answers_3_150",
    #                              "answers_2_example",
    #                              "answers_2_120",
    #                              "answers_3_max_210",
    #                              "answers_1_min_30",
    #                          ]
    #                          )
    # def test_CAH(self, auth_serb, answer):
    #     auth_serb.create_test_go_to_test_CAH()
    #     auth_serb.select_test_CAH()
    #     auth_serb.skip_manual()
    #     for answer_key in answer:
    #         class_name, text = CAH.transcript[answer_key]
    #         auth_serb.click_by_answer(class_name, text)
    #         auth_serb.save_answer_in_test()
    #     auth_serb.expect_notification_completed_test()
    #     auth_serb.go_to_page_doctor()
    #     auth_serb.check_interpretation_for_test(answer)

    # @pytest.mark.parametrize('answer', [
    #                                             MMIL.answer_test_yes,
    #                                             MMIL.answer_test_no,
    #                                             MMIL.answer_test_less,
    #                                             MMIL.answer_exampl,
    #                                             ],
    #                          ids=[
    #                              "answer_test_yes",
    #                              "answer_test_no",
    #                              "answer_test_less",
    #                              "answer_exampl",
    #                          ]
    #                          )
    # def test_MMIL(self, auth_serb, answer):
    #     auth_serb.create_test_go_to_test_MMIL()
    #     auth_serb.select_test_MMIL()
    #     auth_serb.skip_manual()
    #     for answer_key in answer:
    #         class_name, text = MMIL.transcript[answer_key]
    #         auth_serb.click_by_answer(class_name, text)
    #         auth_serb.save_answer_in_test()
    #     auth_serb.expect_notification_completed_test()
    #     auth_serb.go_to_page_doctor()

    # def test_IIG(self, auth_serb):
    #     auth_serb.create_test_go_to_test_IIG()
    #     auth_serb.select_test_IIG()
    #     auth_serb.skip_manual()
    #     auth_serb.fill_all_input_fields_IIG()
    #     auth_serb.save_answer_in_test()
    #     auth_serb.expect_notification_completed_test()
    #
    # def test_BPC(self, auth_serb):
    #     auth_serb.create_test_go_to_test_BPC()
    #     auth_serb.select_test_BPC()
    #     auth_serb.fill_all_input_fields_BPC()
    #     auth_serb.save_answer_in_test()
    #     auth_serb.expect_notification_completed_test()
    #
    # def test_ITRAC(self, auth_serb):
    #     auth_serb.create_test_go_to_test_ITREC()
    #     auth_serb.select_test_ITRAC()
    #     auth_serb.fill_all_input_fields_ITRAC()
    #     auth_serb.save_answer_in_test()
    #     auth_serb.expect_notification_completed_test()

    # def test_delete(self, auth_serb):
    #     auth_serb.delete_all_obs('Ланцов Даниил Андреевич')

    @pytest.mark.parametrize('answer', [
                                        # OKO.answer_min,
                                        # OKO.answer_all_max,
                                        # OKO.answer_0_less_limit,
                                        OKO.answer_all_limit,
                                        ],
                             ids=[
                                 # "answer_min",
                                 # "answer_all_max",
                                 # "answer_0_less_limit",
                                 "answer_all_limit",
                             ]
                             )
    def test_OKO(self, auth_serb, answer):
        auth_serb.create_test_go_to_test_OKO()
        auth_serb.select_test_OKO()
        auth_serb.skip_manual()
        for answer_key in answer:
            class_name, text = OKO.transcript[answer_key]
            auth_serb.click_by_answer(class_name, text)
            auth_serb.save_answer_in_test()
        auth_serb.expect_notification_completed_test()
        auth_serb.go_to_page_doctor()
        auth_serb.check_interpretation_for_test_OKO(answer)
