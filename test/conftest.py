# -*- coding: utf-8 -*-
__author__ = 'Mio4kon'
import pytest


@pytest.fixture(scope="session")
def count():
    print('init count')
    yield 10
    print('teardown count')
