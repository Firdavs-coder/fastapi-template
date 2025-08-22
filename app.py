from fastapi import FastAPI, Depends

from module.routers import router_name
from module.errors.exceptions import HandlingErrors
from module import authorize
from module.errors.responses import Responses

app = FastAPI(
    dependencies=[Depends(authorize)],
    responses=Responses.get_responses()
)

HandlingErrors(app)

app.include_router(router_name)
