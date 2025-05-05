import pytest


@pytest.fixture
def before_after():
    print("Before Test")
    yield
    print("\nAfter Test")





def test_demo1():
    assert 1 == 1

def test_demo2(before_after):
    assert 2 == 3

def test_demo3():
    assert 3 == 3
