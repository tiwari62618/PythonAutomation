import pytest
import allure
import requests


@allure.title("TC# - verify that 2-2==0")
@allure.description("This is a basic Math test")
@pytest.mark.smoke
def test_basic_math():
    assert 2-2==0

@allure.title("TC# - verify that 3-3==0")
@allure.description("This is a regression Testcase which check - verify that 3-3==0")
@pytest.mark.regression
def test_sub1():
    assert 3-3==0

@allure.title("TC# - verify that 1-1==0")
@allure.description("This is a smoke Testcase which check - verify that 1-1==0")
@pytest.mark.smoke
def test_sub2():
    assert 1-1==0

