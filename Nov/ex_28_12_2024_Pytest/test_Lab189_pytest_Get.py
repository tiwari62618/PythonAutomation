import allure
import pytest
import requests


@allure.title("Verify the GET request for Restful Booker")
@allure.description("This test case check Booking 1 and verify the response")
@pytest.mark.positive
def test_get_request_positive():
    URL_get="https://restful-booker.herokuapp.com/booking/1"
    response_data=requests.get(url=URL_get)
    print(response_data.text)
    assert response_data.status_code==200

@allure.title("Verify the GET request for Restful Booker with invalid id")
@allure.description("This test case check Booking -1 and verify the response")
@pytest.mark.negative
def test_get_request_negative():
    URL_get="https://restful-booker.herokuapp.com/booking/-1"
    response_data=requests.get(url=URL_get)
    print(response_data.text)
    assert response_data.status_code==404




