import allure
import pytest


@allure.title("Verify that create booking, with valid data is working")
@allure.description("This test case check for the positive create booking")
@pytest.mark.positive
def test_create_booking_positive():
    print("Test2")
    assert 1+1==3

@allure.title("Verify that create booking, with invalid data is working")
@allure.description("This test case check for the negative create booking")
@pytest.mark.negative
def test_create_booking_negative_1():
    print("Test3")
    assert 1+1==2

@allure.title("Verify that create booking, with invalid data is working")
@allure.description("This test case check for the negative create booking")
@pytest.mark.negative
def test_create_booking_negative_2():
    print("Test3")
    assert 1+1==2



