import pytest
from core.utils.files_helpers.CAH_data import *


class TestMMIL:

    @pytest.mark.parametrize('interpretation', [
                                                # interpretation_1_34,
                                                # interpretation_1_60,
                                                # interpretation_1_90,
                                                interpretation_2_96,
                                                # interpretation_2_102,
                                                # interpretation_2_105,
                                                # interpretation_2_120,
                                                # interpretation_2_135,
                                                # interpretation_2_138,
                                                # interpretation_3_144,
                                                # interpretation_3_150,
                                                # interpretation_2_example,
                                                # interpretation_3_max_210,
                                                # interpretation_1_min_30,
                                                ],
                             ids=[
                                 # "interpretation_1_34",
                                 # "interpretation_1_60",
                                 # "interpretation_1_90",
                                 # "interpretation_2_105",
                                 # "interpretation_2_120",
                                 # "interpretation_2_135",
                                 # "interpretation_2_138",
                                 # "interpretation_3_144",
                                 # "interpretation_3_150",
                                 # "interpretation_2_example",
                                 # "interpretation_2_120",
                                 # "interpretation_3_max_210",
                                 # "interpretation_1_min_30",
                             ]
                             )
    def test_CAH(self, page_t, interpretation):
        page_t.log_in_and_create_test_go_to_test_CAH()
        page_t.select_test_CAH()
        page_t.skip_manual()
        for answer_key in interpretation:
            class_name, text = transcript[answer_key]
            page_t.click_by_answer(class_name, text)
            page_t.save_answer_in_test()
        page_t.expect_notification_completed_test()
        page_t.go_to_page_doctor()
        page_t.check_interpretation_for_test(interpretation)


