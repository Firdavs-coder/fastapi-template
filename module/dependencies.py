from fastapi import Header

async def authorize(ApiKey: str = Header(...)):
    if ApiKey != "123":
        raise PermissionError("Unauthorized request")
