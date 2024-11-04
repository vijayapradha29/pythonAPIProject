import requests
import pytest
import openpyxl
from src.constants.api_constants import url_create_token
from src.helpers.utils import common_headers_json


def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    for rows in sheet.iter_rows(min_row=2, values_only=True):
        username, password = rows
        credentials.append({"username": username,"password": password})
    return credentials


def make_request_auth(username, password):
    payload = {
        "username": username,
        "password": password
    }
    response = requests.post(url=url_create_token(), headers=common_headers_json(), json=payload)
    return response

@pytest.mark.parametrize("user_cred",read_credentials_from_excel("/Users/Dhivya/PycharmProjects/pythonAPIProject/tests/datadriventesting/input.xlsx"))
def test_post_create_token(user_cred):
    username=user_cred["username"]
    password=user_cred["password"]
    response=make_request_auth(username,password)
    assert response.status_code==200