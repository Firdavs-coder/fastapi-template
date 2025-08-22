from fastapi import APIRouter, Depends, UploadFile,  BackgroundTasks
from fastapi.responses import FileResponse, StreamingResponse
from io import BytesIO

from module.params import Params

router = APIRouter()

def write_log(message: str):
    with open("log.txt", "a") as f:
        f.write(message + "\n")

@router.post("/create-user/")
async def create_user(user: dict = Depends(Params.user_form)):
    return {"message": "User created successfully", "user": user}


@router.post("/value-error/")
async def value_error_endpoint():
    raise ValueError("This is a custom value error")

@router.post(
    "/image/",
    responses={
        200: {
            "description": "Successful Response",
            "content": {
                "image/*": {
                    "schema": {
                        "type": "string",
                        "format": "binary"
                    },
                    "example": "<binary image data>"
                }
            }
        }
    }
)
async def image_upload(image: UploadFile = Depends(Params.image_upload)):
    content = await image.read()
    return StreamingResponse(BytesIO(content), media_type=image.content_type)

@router.post("/video/")
async def video_upload(video: UploadFile = Depends(Params.video_upload)):
    content = await video.read()
    return FileResponse(BytesIO(content), media_type=video.content_type, filename=video.filename)

@router.post("/notify/")
async def notify(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, "Notification sent")
    return {"message": "Notification will be logged in the background"}
