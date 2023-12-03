# import function from helpers.py
from routers.helpers import check_user_authentication


def test_check_user_authentication_admin():
    # Arrange
    user = {"user_role": "admin"}
    # Act
    check_user_authentication(user)
    # Assert
    assert True


def test_check_user_authentication_developer():
    # Arrange
    user = {"user_role": "developer"}
    # Act
    check_user_authentication(user)
    # Assert
    assert True


def test_check_user_authentication_business_owner():
    # Arrange
    user = {"user_role": "business_owner"}
    # Act
    check_user_authentication(user)
    # Assert
    assert True
