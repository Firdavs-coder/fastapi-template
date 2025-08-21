from fastapi import FastAPI, Depends

from module.routers import router_name
from module.errors.exceptions import HandlingErrors
from module import authorize

app = FastAPI(dependencies=[Depends(authorize)])

HandlingErrors(app)

app.include_router(router_name)
