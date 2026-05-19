import json
from operator import add, sub, mul, truediv
from calc_data import get_calc_data
from logging_config import logger
_operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}
def _get_response(code, body):
    return {
        'statusCode': code,
        'body': json.dumps(body)
    }

def lambda_handler(event, context):
    """
    handling calculating from JSON with following structure:
    { "op1": < float number >, "op2": < float number >, "operation" : < string [+/*-] >} 

    Args:
        event (_type_): event from HTTP API Gateway
        context (_type_): context from AWS Lambda
    """
    logger.debug("Received event: %s", event)
    body = event.get('body', None)
    response = _get_response(400, 'missing body')
    if  body:
        try:
            data = get_calc_data(body)
            logger.debug(f"Parsed data: {data}")
            result = _operations[data.operation](data.op1, data.op2)
            response = _get_response(200, result)
        except ValueError as e:
            response = _get_response(400, str(e))
        except KeyError:
            response = _get_response(404, f"operation {data.operation} not found")
        except ZeroDivisionError:
            response = _get_response(400, 'division by zero')
    return response