
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi import Request
from fastapi.responses import JSONResponse

class HandlingErrors:
    def __init__(self, app: FastAPI):
        self.app = app

        self.app.add_exception_handler(RequestValidationError, self.validation_exception_handler)
        self.app.add_exception_handler(ValueError, self.custom_exception_handler)
        self.app.add_exception_handler(PermissionError, self.permission_error_handler)

    @staticmethod
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        error = exc.errors()
        return JSONResponse(
            status_code=422,
            content={
                "error": "Validation failed",
                "message": error[0]['msg'],
            },
        )

    @staticmethod
    async def custom_exception_handler(request: Request, exc: ValueError):
        return JSONResponse(
            status_code=400,
            content={
                "error": "Custom error",
                "message": str(exc),
            },
        )

    @staticmethod
    async def permission_error_handler(request: Request, exc: PermissionError):
        return JSONResponse(
            status_code=401,
            content={
                "error": "Unauthorized",
                "message": str(exc),
            },
        )

    @staticmethod
    async def internal_server_error_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={
                "error": "Internal Server Error",
                "message": "An unexpected error occurred",
            },
        )