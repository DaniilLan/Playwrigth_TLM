import time

import pytest
from core.utils.file_helpers import *


class TestMMIL:

    def test_CAH(self, page_t):
        page_t.log_in_and_create_test_go_to_test_CAH()
        page_t.select_test_CAH()
        page_t.skip_manual()
        for answer_key in interpretation_b:
            class_name, text = transcript[answer_key]
            page_t.click_by_answer(class_name, text)
            page_t.save_answer_in_test()
        page_t.wait_visible_notification()


