import pytest
@pytest.mark.login
def test_login_test():
    print("This is login test")
    assert False
def logout_test():
    print("This is logout test")
    assert True