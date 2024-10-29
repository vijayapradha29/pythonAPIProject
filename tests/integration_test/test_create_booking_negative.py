from imaplib import Flags

import requests
import pytest
from src.helpers.api_requests_wrapper import post_requests
from src.constants.api_constants import url_create_booking,base_url
from src.helpers.utils import common_headers_json
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import verify_http_status_code
class TestCreateBookingNegative(object):
    def test_create_booking_Positive_tc1(self):
        response1=post_requests(url=url_create_booking(),auth=None,headers=common_headers_json(),payload=payload_create_booking(),in_json=False)
        verify_http_status_code(response1,200)
        print(response1.json())
    def test_create_booking_negative_tc2(self):
        response1=post_requests(url=url_create_booking(),auth=None,headers=None,payload=payload_create_booking(),in_json=False)
        verify_http_status_code(response1,500)
    def test_create_booking_negative_tc3(self):
        response1=post_requests(url=url_create_booking(),auth=None,headers=common_headers_json(),payload="Null",in_json=False)
        verify_http_status_code(response1,400)
    def test_create_booking_negative_tc4(self):
        response1=post_requests(url=base_url(),auth=None,headers=common_headers_json(),payload=payload_create_booking(),in_json=False)
        verify_http_status_code(response1,404)