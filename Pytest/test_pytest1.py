import pytest


def test_m1(setup):
    print("Method 1")

def test_m2():
    print("Method 2")

def test_m3():
    print("Method 3")

def test_demo1():
    print("Demo1")

def test_demo2():
    print("Demo2")

@pytest.mark.smoke
def test_smoke():
    print("Smoke test")

@pytest.mark.skip
def test_snaity():
    print("Sanity test")

#This method will fail marking to skip the failed one to reported
@pytest.mark.xfail
def test_validations():
    a=2
    b=3
    assert a==b
    print("Validation method")