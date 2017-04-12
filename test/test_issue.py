# -*- coding: utf-8 -*-
__author__ = 'Mio4kon'

import pytest


@pytest.allure.issue('http://jira.lan/browse/ISSUE-1')
def test_foo():
    assert False


import allure


@allure.issue('http://jira.lan/browse/ISSUE-2')
class TestBar:
    # test will have ISSUE-2, ISSUE-3 and ISSUE-4 label
    @allure.issue('http://jira.lan/browse/ISSUE-3')
    def test_bar1(self):
        # You can use this feature like a function inside the test
        allure.dynamic_issue('http://jira.lan/browse/ISSUE-4')
        pass

    # test will have only ISSUE-2 label
    def test_bar2(self):
        pass
