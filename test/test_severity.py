# -*- coding: utf-8 -*-
__author__ = 'Mio4kon'

import pytest


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
def test_minor():
    assert False


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
class TestBar:
    # will have CRITICAL priority
    def test_bar(self):
        pass

    # will have BLOCKER priority via a short-cut decorator
    @pytest.allure.BLOCKER
    def test_bar(self):
        pass
