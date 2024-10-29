from http.client import responses

from src.helpers.api_requests_wrapper import post_requests
from src.constants.api_constants import url_create_booking
from src.helpers.common_verification import verify_http_status_code,verify_response_should_not_be_none
from src.helpers.utils import common_headers_json
from src.helpers.payload_manager import payload_create_booking
import requests
import pytest


class TestCreateBooking(object):
    @pytest.mark.positive
    def test_create_booking_tc1(self):
        response = post_requests(url=url_create_booking(), headers=common_headers_json(), auth=None,
                                 payload=payload_create_booking(), in_json=False)
        print(response)
        verify_response_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, 200)
        bookingid=response.json()["bookingid"]
        print(bookingid)

    @pytest.mark.negative
    def test_create_booking_tc2(self):
        response=post_requests(url=url_create_booking(),headers=common_headers_json(),auth=None,payload={},in_json=False)
        verify_http_status_code(response,500)