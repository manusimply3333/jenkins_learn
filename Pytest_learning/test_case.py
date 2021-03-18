import pytest

def test_Case1():
    a = 10
    b = 20
    assert a == b - 10
@pytest.mark.login
def test_Case2():
    a = 'String'
    b = str
    assert type(a) == b
def test_Case3():
    a = 10
    b = "10"
    assert a == b,"Types are different"
@pytest.mark.login
def test_Case_login1():
    assert True
def test_Case_login2():
    assert False
