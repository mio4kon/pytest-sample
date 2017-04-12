# -*- coding: utf-8 -*-
__author__ = 'Mio4kon'

import pytest


@pytest.allure.testcase('http://my.tms.org/TESTCASE-1')
def test_foo():
    assert False


import allure


@allure.testcase('http://my.tms.org/browse/TESTCASE-2')
class TestBar:
    # test will have TESTCASE-2 and TESTCASE-3 label
    @allure.testcase('TESTCASE-3')
    def test_bar1(self):
        pass

    # test will have only TESTCASE-2 label
    def test_bar2(self):
        pass
