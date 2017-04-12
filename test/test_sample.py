# -*- coding: utf-8 -*-
__author__ = 'Mio4kon'
import allure


class TestSample:
    def test_login(self):
        allure.attach('描述', '这是一个注册登录的case')
        self.register()
        result = self.login('mio4kon')
        assert result

    @allure.step(title="登录账号:{1}")
    def login(self, account):
        return True

    @allure.step(title="注册")
    def register(self):
        pass
