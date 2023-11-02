from fastapi import APIRouter
from fastapi.responses import PlainTextResponse


router = APIRouter(tags=['Logs'])

@router.get('/logs', response_class=PlainTextResponse)
async def get_logs():
    with open("debug.log", "r") as f:
        log = '\n'.join(f.readlines())
    return log
