import allure


class Test_Allure:
    @allure.step(title="第一个游戏")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_001(self):
        allure.attach("描述", "测试显示")
        assert 1
