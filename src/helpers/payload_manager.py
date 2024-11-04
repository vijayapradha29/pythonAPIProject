from faker import Faker
import json

from faker.contrib.pytest.plugin import faker

faker=Faker()

def payload_create_booking():
    payload={
            "firstname": "120000",
            "lastname": "456",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }

    return payload

def payload_create_booking_dynamic():
    json_payload={
            "firstname":faker.first_name(),
            "lastname":faker.last_name(),
            "totalprice":faker.random_int(100,1000),
            "depositpaid":faker.boolean(),
            "bookingdates": {
                "checkin":str(faker.date_between('-3y','today')),
                "checkout":str(faker.date_between('today','+3y'))
            },
            "additionalneeds":faker.random_element(elements=("Breakfast","Wifi","Extra Bed","Parking"))
        }

    return json_payload

def payload_create_token():
    payload={
    "username" : "admin",
    "password" : "password123"
}
    return payload