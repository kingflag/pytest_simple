import pytest
import requests

# curl --location --request GET 'https://echo.apifox.com/get?q1=v1&q2=v2'
def test_apifox_get_api():
    """test apifox get api"""
    # build request parameters
    params = {
        'q1': 'v1',
        'q2': 'v2'
    }
    
    # send get request
    url = 'https://echo.apifox.com/get'
    response = requests.get(url, params=params)
    
    # verify response
    assert response.status_code == 200
    json_response = response.json()
    assert json_response['args']['q1'] == 'v1'
    assert json_response['args']['q2'] == 'v2'
    assert 'headers' in json_response
    assert 'url' in json_response


# curl --location --request POST 'https://echo.apifox.com/post?q1=v1&q2=v2' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#     "d": "deserunt",
#     "dd": "adipisicing enim deserunt Duis"
# }'

def test_apifox_post_api():
    """tets apifox post api"""
    # build request parameters
    query_params = {
        'q1': 'v1',
        'q2': 'v2'
    }
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        'd': 'deserunt',
        'dd': 'adipisicing enim deserunt Duis'
    }
    
    # send post request
    response = requests.post(
        'https://echo.apifox.com/post',
        params=query_params,
        headers=headers,
        json=payload
    )
    
    # verify response
    assert response.status_code == 200, "HTTP状态码应为200"
    response_data = response.json()
    
    # verify query parameters
    assert response_data['args']['q1'] == 'v1'
    assert response_data['args']['q2'] == 'v2'
    
    # verify payload data
    assert response_data['json']['d'] == 'deserunt'
    assert response_data['json']['dd'] == 'adipisicing enim deserunt Duis'
    
    # verify base response structure
    assert 'headers' in response_data
    assert 'url' in response_data
    assert response_data['url'] == 'http://echo.apifox.com/post?q1=v1&q2=v2'


# curl --location --request DELETE 'https://echo.apifox.com/delete?q1=v1' \
# --form 'b1="v1"' \
# --form 'b2="v2"'
def test_apifox_delete_api():
    """Test DELETE request API"""
    # Request parameters
    query_params = {
        'q1': 'v1'
    }
    files = {
        'b1': (None, 'v1'),
        'b2': (None, 'v2')
    }
    
    # Send request
    response = requests.delete(
        'https://echo.apifox.com/delete',
        params=query_params,
        files=files
    )
    
    # Verify response
    assert response.status_code == 200, "HTTP status code should be 200"
    response_data = response.json()
    
    # Verify query parameters
    assert response_data['args']['q1'] == 'v1'
    
    # Verify form data
    assert response_data['form']['b1'] == 'v1'
    assert response_data['form']['b2'] == 'v2'
    
    # Verify basic response structure
    assert 'headers' in response_data
    assert 'url' in response_data
    assert response_data['url'].endswith('echo.apifox.com/delete?q1=v1')
    assert response_data['data'] == ""
    assert response_data['files'] == {}
    assert response_data['json'] is None


# curl --location --request PUT 'https://echo.apifox.com/put' \
# --header 'Content-Type: text/plain' \
# --data-raw 'test value'
def test_apifox_put_api():
    """Test PUT request API"""
    # Request parameters
    query_params = {
        'q1': 'v1'
    }
    headers = {
        'Content-Type': 'text/plain'
    }
    data = 'test value'
    
    # Send request
    response = requests.put(
        'https://echo.apifox.com/put',
        params=query_params,
        headers=headers,
        data=data
    )
    
    # Verify response
    assert response.status_code == 200, "HTTP status code should be 200"
    response_data = response.json()
    
    # Verify query parameters
    assert response_data['args']['q1'] == 'v1'
    
    # Verify request data
    assert response_data['data'] == 'test value'
    
    # Verify basic response structure
    assert 'headers' in response_data
    assert 'url' in response_data
    assert response_data['url'].endswith('echo.apifox.com/put?q1=v1')
    assert response_data['files'] == {}
    assert response_data['form'] == {}
    assert response_data['json'] is None


# curl --location --request PATCH 'https://echo.apifox.com/patch?q1=v1' \
# --header 'Content-Type: application/json' \
# --data-raw ''
def test_apifox_patch_api():
    """Test PATCH request API"""
    # Request parameters
    query_params = {
        'q1': 'v1'
    }
    headers = {
        'Content-Type': 'application/json'
    }
    
    # Send request
    response = requests.patch(
        'https://echo.apifox.com/patch',
        params=query_params,
        headers=headers,
        data=''
    )
    
    # Verify response
    assert response.status_code == 200, "HTTP status code should be 200"
    response_data = response.json()
    
    # Verify query parameters
    assert response_data['args']['q1'] == 'v1'
    
    # Verify request data
    assert response_data['data'] == ""
    
    # Verify basic response structure
    assert 'headers' in response_data
    assert 'url' in response_data
    assert response_data['url'].endswith('echo.apifox.com/patch?q1=v1')
    assert response_data['files'] == {}
    assert response_data['form'] == {}
    assert response_data['json'] is None