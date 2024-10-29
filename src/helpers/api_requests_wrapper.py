import json
# import json

import requests

def get_requests(url,auth,in_json):
    get_response=requests.get(url=url, auth=auth)
    if in_json is True:
        return get_response.json()
    return get_response

def post_requests(url,auth,headers,payload,in_json):
    post_response=requests.post(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return post_response

def patch_requests(url,auth,headers,payload,in_json):
    patch_response=requests.patch(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return patch_response.json()
    return patch_response

def put_requests(url,auth,headers,payload,in_json):
    put_response=requests.put(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return put_response.json()
    return put_response

def delete_requests(url,auth,headers,payload,in_json):
    delete_response=requests.delete(url=url, auth=auth, headers=headers)
    if in_json is True:
        return delete_response.json()
    return delete_response