# -*- coding: utf-8 -*-
__author__ = 'Mio4kon'


class TestSample2:
    def test_answer(self, count):
        print('test_answer get count %s' % count)
        assert count == 10

    def test_answer_2(self, count):
        print('test_answer_2 get count %s' % count)
        assert count == 10
