import json
from operator import add, sub, mul, truediv
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
def _validate_body(body):
    errorMessage=""
    if any(field not in body for field in ['op1', 'op2', 'operation']):
        if 'op1' not in body:
            errorMessage += "field op1 is missing. "
        if 'op2' not in body:
            errorMessage += "field op2 is missing. "
        if 'operation' not in body:
            errorMessage += "field operation is missing. "
    else:
        if not isinstance(body['op1'], (int, float)):
            errorMessage += "op1 not a number. "
        if not isinstance(body['op2'], (int, float)):
            errorMessage += "op2 not a number. "
    return errorMessage
def lambda_handler(event, context):
    """
    handling calculating from JSON with following structure:
    { "op1": < float number >, "op2": < float number >, "operation" : < string [+/*-] >} 

    Args:
        event (_type_): event from HTTP API Gateway
        context (_type_): context from AWS Lambda
    """
    body = event.get('body', None)
    response = _get_response(400, 'missing body')
    if  body:
        try:
            bodyObj = json.loads(body)
            errorMessage = _validate_body(bodyObj)
            if errorMessage:
                response = _get_response(400, errorMessage)
            else:
                op1 = bodyObj['op1']
                op2 = bodyObj['op2']
                operation = bodyObj['operation']
                result = _operations[operation](op1, op2)
                response = _get_response(200, result)
        except json.JSONDecodeError:
            response = _get_response(400, 'invalid JSON')
        except KeyError:
            response = _get_response(404, f"operation {operation} not found")
        except ZeroDivisionError:
            response = _get_response(400, 'division by zero')
    return response