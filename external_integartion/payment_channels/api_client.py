import requests
import logging

logger = logging.Logger("request_handler_logger")


class APIClient:
    headers = {"Content-Type": "application/json"}

    @classmethod
    def get(cls, url: str, headers: dict) -> str:
        response = requests.get(url, headers=headers)
        logger.info(
            f"GET request perform on : URL: {url}, RESPONSE: {response.text}, STATUS CODE: {response.status_code}")
        if response.status_code != 200 and response.status_code != 201:
            logger.error(msg=f"Something went wrong while performing API Request, {url}")
            raise Exception(f"Error while performing a request on url: {url}")

        logger.info(msg=f"Performing GET request: {url} response, {response.text}")
        return response.text

    @classmethod
    def post(cls, url: str, body: dict, headers: dict) -> str:
        response = requests.post(url, headers=headers, data=body, verify=False)
        logger.info(
            f"POST request perform on : URL: {url}, RESPONSE: {response.text}, STATUS CODE: {response.status_code}")

        if response.status_code != 200 and response.status_code != 201:
            # logger.error(msg=f"Something went wrong while performing API Request", request=body)
            raise Exception(
                f"Error while performing a request on url: {url}, response: {response.text}, STATUS: {response.status_code}")

        logger.info(msg=f"Performing POST request: {url} response, {response.text}")
        return response.text

    @classmethod
    def delete(cls, url: str, body: dict, headers: dict) -> str:
        response = requests.delete(url, headers=headers, verify=False)
        logger.info(
            f"DELETE request perform on : URL: {url}, RESPONSE: {response.text}, STATUS CODE: {response.status_code}")

        if response.status_code != 200 and response.status_code != 201:
            # logger.error(msg=f"Something went wrong while performing API Request", request=body)
            raise Exception(
                f"Error while performing a request on url: {url}, response: {response.text}, STATUS: {response.status_code}")

        logger.info(msg=f"Performing DELETE request: {url} response, {response.text}")
        return response.text
