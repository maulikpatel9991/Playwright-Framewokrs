from Utils.logger import logger1
from Utils.configutils import get_api_url


def get_request(api_request_context, api_endpoint, query_params=None, header=None):
    """
    Perform simple HTTP Get request
    :param api_request_context: The request context
    :param base_url: The base URL of the API
    :param api_endpoint: The endpoint of the API
    :param query_params: Dictionary of query parameters to be sent with the GET request
    :param header: Dictionary of headers to be sent with the GET request
    :return: The response object
    """
    url = get_api_url() + api_endpoint
    logger1.info(f"Performing GET request to {url} with query_params: {query_params} and headers: {header}")

    try:
        response = api_request_context.get(url, params=query_params, headers=header)
        return response
    except Exception as e:
        log.error(f"Error during GET request to {url}: {e}")
        raise



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

def put_request(api_request_context,api_endpoint, payload, header=None):
    """
        Method to perform HTTP Put request with body data, header is optional
        :param api_request_context:
        :param base_url:
        :param api_endpoint:
        :param payload:
        :param header:
        :return:
        """
    url = get_api_url() + api_endpoint
    log.info(f"Performing PUT request to {url} with payload: {payload} and headers: {header}")
    try:
        response = api_request_context.put(url, data=payload, headers=header)
        return response
    except Exception as e:
        log.error(f"Error during put request to {url}: {e}")
        raise

def patch_request(api_request_context, api_endpoint, payload, header=None):
    """
        Method to perform HTTP Patch request with body data, header is optional
        :param api_request_context:
        :param base_url:
        :param api_endpoint:
        :param payload:
        :param header:
        :return:
        """
    url = get_api_url() + api_endpoint
    log.info(f"Performing PATCH request to {url} with payload: {payload} and headers: {header}")
    try:
        response = api_request_context.patch(url, data=payload, headers=header)
        return response
    except Exception as e:
        log.error(f"Error during put request to {url}: {e}")
        raise

def delete_request(api_request_context, api_endpoint, header=None, query_params=None):
    """
        Method to perform simple HTTP Delete request. The headers and params are optional.
        :param api_request_context:
        :param base_url:
        :param api_endpoint:
        :param header:
        :param query_params:
        :return:
        """
    url = get_api_url() + api_endpoint
    log.info(f"Performing PATCH request to {url} with payload: {query_params} and headers: {header}")
    try:
        response = api_request_context.delete(url, headers=header, params=query_params)
        return response
    except Exception as e:
        log.error(f"Error during delete request to {url}: {e}")
        raise