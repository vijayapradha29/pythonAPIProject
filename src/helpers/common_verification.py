def verify_http_status_code(response_data,expect_data):
    assert response_data.status_code==expect_data,"Expected HTTP Status Code"+expect_data

def verify_json_key_not_null(key):
    assert key!=0,"Key is Non Empty"+key
    assert key>0,"Key is Greater than Zero"

def verify_response_should_not_be_none(key):
    assert key is not None

def verify_response_time():
    pass