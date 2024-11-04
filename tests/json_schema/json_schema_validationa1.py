import json

import jsonschema

# from http.client import responses

# from jsonschema.benchmarks.contains import schema

from src.helpers.api_requests_wrapper import post_requests
from src.constants.api_constants import url_create_booking
from src.helpers.common_verification import verify_http_status_code, verify_response_should_not_be_none
from src.helpers.utils import common_headers_json
from src.helpers.payload_manager import payload_create_booking
import requests
import pytest
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import os

class TestCreateBooking(object):

    def load_schema(self, schema_file):
        with open(schema_file, 'r') as file:
            return json.load(file)

    @pytest.mark.positive
    def test_create_booking_jsonschema(self):
        response = post_requests(url=url_create_booking(), headers=common_headers_json(), auth=None,
                                 payload=payload_create_booking(), in_json=False)
        print(response)
        verify_response_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, 200)
        bookingid = response.json()["bookingid"]
        print(bookingid)

        response_json = response.json()
        dir=os.getcwd()
        # print(dir)
        file=os.getcwd()+"/schema.json"
        schema=self.load_schema(file)
        try:
            validate(instance=response_json, schema=schema)
        except ValidationError as e:
            print(e.message)
