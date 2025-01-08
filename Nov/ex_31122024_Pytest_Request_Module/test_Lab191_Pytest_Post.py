import pytest
import allure
import requests

from Nov.ex_07112024_keywords_identifiers_variables.Lab006 import first_name


@allure.title("TC#1 - create booking CRUD Positive")
@allure.description("Verify the create booking!")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    base_url="https://restful-booker.herokuapp.com"
    base_path_post="/booking"

    full_url=base_url+base_path_post
    headers={
        "Content-Type" : "application/json"
    }
    payload={

            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
    response_data = requests.post(url=full_url,headers=headers,json=payload)

    #Status code verification
    assert response_data.status_code==200

    #Booking ID>0, firstname==Jim
    response_data_json=response_data.json()
    bookingid=response_data_json["bookingid"]
    print(bookingid)

    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid) == int

    firstname = response_data_json["booking"]["firstname"]
    assert firstname=="Jim"
    assert type(firstname)==str

    lastname = response_data_json["booking"]["lastname"]
    assert lastname == "Brown"
    assert type(lastname) == str

    totalprice = response_data_json["booking"]["totalprice"]
    assert totalprice == 111
    assert type(totalprice) == int

    depositpaid = response_data_json["booking"]["depositpaid"]
    assert depositpaid == True
    assert type(depositpaid) == bool

    checkin = response_data_json["booking"]["bookingdates"]["checkin"]
    checkout= response_data_json["booking"]["bookingdates"]["checkout"]
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"

    time=response_data.elapsed.total_seconds()
    assert time < 3



@allure.title("TC#2 - create booking CRUD Negative")
@allure.description("Verify the invalid payload Booking is not created!")
@pytest.mark.crud
def test_create_booking_negative_tc1():
    pass
