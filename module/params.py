from fastapi import Form, File, UploadFile

from fastapi.exceptions import RequestValidationError
from pydantic import EmailStr

class Params:
    @staticmethod
    async def user_form(
        name: str = Form(..., min_length=2, max_length=50),
        email: EmailStr = Form(...),
        age: int = Form(..., ge=18, le=120),
        is_active: bool = Form(...)
    ) -> dict:
        if name == "John":
            raise RequestValidationError(errors=[{"msg": "Name 'John' is not allowed"}])

        return {"name": name, "email": email, "age": age, "is_active": is_active}


    @staticmethod
    async def image_upload(image: UploadFile = File(..., description="Upload an image file")) -> UploadFile:
        if image.content_type not in ["image/jpeg", "image/png"]:
            raise RequestValidationError(errors=[{"msg": "Only image files are allowed."}])
        return image

    @staticmethod
    async def video_upload(video: UploadFile = File(..., description="Upload a video file")) -> UploadFile:
        if video.content_type not in ["video/mp4", "video/x-matroska"]:
            raise RequestValidationError(errors=[{"msg": "Only video files are allowed."}])
        return video