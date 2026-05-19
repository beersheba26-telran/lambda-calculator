from os import getenv

from dotenv import load_dotenv
load_dotenv()   

URL_LAMBDA_HANDLER = getenv("URL_LAMBDA_HANDLER", "https://ss0r315yqd.execute-api.us-east-1.amazonaws.com/calculate")