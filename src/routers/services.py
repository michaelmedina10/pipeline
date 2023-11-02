from fastapi import APIRouter
from fastapi.responses import JSONResponse
import json
from utils.handle_file import read_pickle
from utils.logger import logger
from instructions_pipeline.pipeline import pipeline


router = APIRouter(tags=['Services'])

@router.get('/services', response_class=JSONResponse)
async def get_services():
    logger.debug("/services")
    pipeline()
    data = read_pickle()
    response = {}
    for service, dataframe in data.items():
        response[service] = json.loads(dataframe.to_json(orient='records'))
    return response
