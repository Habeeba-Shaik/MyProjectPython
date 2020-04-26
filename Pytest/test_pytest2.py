import pytest


@pytest.mark.usefixtures("user_data","crossBrowser")
class Test_pytest2:

    def test_userProfile(self,user_data):
        print(user_data[1])

    def test_cross_browser(self,crossBrowser):
        print(crossBrowser)