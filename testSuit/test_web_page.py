#Joomag_Task for QA
from pages.basepage import BasePage
import pytest
from pages.mainPage import Mainpage


class TestNumbersElements:

    @pytest.fixture(scope="function", autouse=True)
    def setup(module):
        page = BasePage(module)

    @pytest.mark.need_review
    def test_numbers_of_form(self, browser):
        page = Mainpage(browser)
        page.count_forms()

    @pytest.mark.need_review
    def test_number_of_img_tags(self, browser):
        page = Mainpage(browser)
        page.count_img()

