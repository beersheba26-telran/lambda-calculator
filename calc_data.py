from logging_config import logger
from pydantic import BaseModel, ValidationError, Field
class CalcData(BaseModel):
    op1: float
    op2: float
    operation: str
    
def get_calc_data(dataJson):
    try:
        return CalcData.model_validate_json(dataJson)
    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        raise ValueError(', '.join([f"{error['loc']} {error['msg']}" for error in e.errors()]))
        