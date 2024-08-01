from utilities.API import Response, APIRequest
import pytest
from utilities.readProperties import Read_config
import json


class TestApiCall:
    api_base_url = Read_config.api_url()

    def test_api_test_get_method(self):
        response = APIRequest().get(self.api_base_url)
        print(response)
        assert response.status_code == 200
        print("hello")
    def test_api_test_post_method(self):
        api_url = "https://app.mocklab.io/"
        headers = {
            'Content-Type': 'application/json'
        }

        payload = {
            'name': 'Ram',
            'age': '22'
        }
        payload = json.dumps(payload)
        response = APIRequest().post(api_url, payload, headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        print(f"Response Headers: {response.headers}")
        print(f"Response as_dict: {response.as_dict}")
        assert response.status_code == 200
