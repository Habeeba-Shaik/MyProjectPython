import pytest


@pytest.fixture()
def setup():
    print("I will execute first")
    yield
    print("I will execute at the end")

@pytest.fixture()
def user_data():
    print("User data")
    return ["Habeeba","Shaik"]

@pytest.fixture(params=["Chrome","FireFox","IE"])
def crossBrowser(request):
    return request.param


