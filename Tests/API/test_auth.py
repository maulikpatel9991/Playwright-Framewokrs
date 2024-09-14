from Utils.utils import read_file
from Utils.api_actions import post_request
from Utils.api_validations import validate_response_code, validate_schema
from Utils.api_utilities import get_value_from_response
import pytest
from Utils.utils import shared_data



testcasedata = read_file('createAuth.json')
@pytest.mark.api
@pytest.mark.parametrize("case", testcasedata["positive"])
def test_create_authToken_positive(api_request_context,case):
    """
    Test case for creating an authentication token with positive test data.

    This test verifies that an authentication token is created successfully when valid data is provided.
    It checks that the response has the expected status code and schema, and stores the token ID in shared data.

    Args:
        api_request_context: The API request context provided by the fixture.
        case (dict): A dictionary containing test case data including endpoint, parameters, headers, 
                     expected status code, and expected schema.

    Steps:
        1. Send a POST request to the API endpoint with the provided parameters and headers.
        2. Validate the response status code.
        3. Validate the response schema.
        4. Extract and store the token ID from the response in shared data.
    """
    response = post_request(api_request_context,api_endpoint=case["endpoint"],payload=case["params"],header=case["headers"])
    validate_response_code(response, case["expected_status"])
    validate_schema(response=response, schema=case['expected_schema'])
    shared_data.set_data("token_id", get_value_from_response(response,'token'))


@pytest.mark.api
@pytest.mark.parametrize("case", testcasedata["negative"])
def test_create_authToken_negative(api_request_context,case):
    """
    Test case for creating an authentication token with negative test data.

    This test verifies that the API handles invalid data correctly and responds with the appropriate error
    message and status code. It checks that the response has the expected status code and schema.

    Args:
        api_request_context: The API request context provided by the fixture.
        case (dict): A dictionary containing test case data including endpoint, parameters, headers, 
                     expected status code, and expected schema.

    Steps:
        1. Send a POST request to the API endpoint with the provided parameters and headers.
        2. Validate the response status code.
        3. Validate the response schema.
    """
    response = post_request(api_request_context,api_endpoint=case["endpoint"],payload=case["params"],header=case["headers"])
    validate_response_code(response, case["expected_status"])
    validate_schema(response=response, schema=case['expected_schema'])

    # https://github.com/DipankarDandapat/Playwright_API_Python_Framework/blob/main/testcases/test_1_auth.py