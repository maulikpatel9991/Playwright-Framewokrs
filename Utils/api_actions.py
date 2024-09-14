from Utils.logger import logger1
from Utils.configutils import get_api_url

def post_request(api_request_context, api_endpoint, payload, header=None):
    """
    Perform HTTP Post request with in-line body data
    :param api_request_context: The request context
    :param api_endpoint: The endpoint of the API
    :param payload: The payload to be sent with the POST request
    :param header: Dictionary of headers to be sent with the POST request
    :return: The response object
    """
    url = get_api_url() + api_endpoint
    logger1.info(f"Performing POST request to {url} with payload: {payload} and headers: {header}")

    try:
        response = api_request_context.post(url, data=payload, headers=header)
        return response
    except Exception as e:
        logger1.error(f"Error during POST request to {url}: {e}")
        raise