import requests
import json

from config import URL_LAMBDA_HANDLER
from logging_config import logger
def calculate_request(data:list[str]):
    """request Rest POST for triggering lambda_handler lambda function
       no validation as it's done in lambda_handler
       returns result or error message from lambda_handler response
    Args:
        data (list[str]): list of strings: first - op1 value , second - op2 value , third - operation
        
    """
    logger.debug(f"URL for lambda handler: {URL_LAMBDA_HANDLER}")
    payload = _get_payload(data)
    logger.debug(f"Payload for lambda handler: {payload}")
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", URL_LAMBDA_HANDLER, headers=headers, data=payload)
    logger.debug(f"Response from lambda handler: {response.status_code}, {response.text}")
    if response.status_code == 200:
        print(f"result={response.json()}")
    else:
        print(f"Error: status_code={response.status_code}, response={response.json()}")

def _get_payload(data):
    payload = json.dumps({
        "op1": float(data[0]),
        "op2": float(data[1]),
        "operation": data[2]
    })
    
    return payload