import os

import requests
import json
import pytest
from jsonschema import validate
from request import *


@pytest.fixture()
def request_config():
    return Request()


@pytest.fixture()
def expected_response_body():
    with open(file=f"{os.getcwd()}/expected_response_body.json") as f:
        content = f.read()
    return json.loads(content)


@pytest.fixture()
def response_schema():
    with open(file=f"{os.getcwd()}/schema.json") as f:
        content = f.read()
    return json.loads(content)


class TestAPI:

    def test_status_OK(self, request_config):

        response = requests.post(**request_config.config)

        assert response.ok

    def test_response_data_schema_validation(self,
                                             request_config,
                                             response_schema):

        response = requests.post(**request_config.config)

        response_body = json.loads(response.text)

        assert not validate(instance=response_body, schema=response_schema)

    @pytest.mark.parametrize('password', ['wrong', ' '])
    def test_wrong_password(self,
                            request_config,
                            password):

        request_config.set_payload(password=password)

        response = requests.post(**request_config.config)

        assert response.status_code == 400

    @pytest.mark.parametrize('url_suffix', ['wrong', ' '])
    def test_wrong_password(self,
                            request_config,
                            url_suffix):

        request_config.set_url(url_suffix=url_suffix)

        response = requests.post(**request_config.config)

        assert response.status_code == 404

    @pytest.mark.xfail
    def test_response_data_validation(self,
                                      request_config,
                                      expected_response_body):

        response = requests.post(**request_config.config)

        response_body = json.loads(response.text)

        assert expected_response_body == response_body

