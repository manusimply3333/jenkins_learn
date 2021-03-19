import pytest

@pytest.fixture
def main_module():
    a = 10
    b = 20
    c = a + b
    return c

def test_first(main_module):
    assert 30 == main_module

def test_second(main_module):
    assert main_module !=40


def test_first(main_module):
    assert 30 == main_module


def test_second(main_module):
    assert main_module != 40

def test_second(main_module):
    a = "40"
    assert main_module == int(a)
