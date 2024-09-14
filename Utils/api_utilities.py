from jsonpath_ng import parse
from Utils.logger import logger1


def get_response_code(response):
    """
    Method to get response code
    :param response:
    :return:
    """
    try:
        status_code_value = response.status
        logger1.info(f'API executed successfully and the response code: {status_code_value}')
        return status_code_value
    except Exception as e:
        logger1.info('The error is ', e)

def get_response_data(response):
    """
    Method to get response data
    :param response:
    :return:
    """
    try:
        response_data = response.json()
        logger1.info(f'API executed successfully and the response data is {response_data}')
        return response_data
    except Exception as e:
        try:
            response_data = response.text
            logger1.info(f'API executed successfully and the response data is {response_data}')
            return response_data
        except Exception as e:
            logger1.info('The error is ', e)

def get_value_from_response(response, jsonpath_expression):
    """
    Method to get the value from JSON response by passing valid JSON path expression.
    :param jsonpath_expression:
    :param response:
    :return:
    """
    try:
        api_response = get_response_data(response)
        parsed_expression = parse(f'$.{jsonpath_expression}')
        match = parsed_expression.find(api_response)
        logger1.info(f'API executed successfully and the response value in {jsonpath_expression} is {match[0].value}')
        return match[0].value
    except Exception as e:
        logger1.info('The error is ', e)

