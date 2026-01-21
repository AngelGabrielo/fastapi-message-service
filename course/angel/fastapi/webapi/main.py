from fastapi.exceptions import RequestValidationError
from starlette import status
from fastapi.responses import JSONResponse

from course.angel.fastapi.webapi.config.db import Base, engine
from course.angel.fastapi.webapi.routers import messages

from fastapi import FastAPI, Request
import course.angel.fastapi.webapi.entities

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(messages.router, prefix="/messages", tags=["messages"])

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    custom_errors = []
    for error in exc.errors():
        loc = error.get("loc", [])
        field_name = loc[-1] if loc else 'unknown'

        custom_errors.append({
            'message': error.get('msg','Validation error'),
            'field': str(field_name),
            'type': error.get('type','Validation error')
        })

    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, content={"errors": custom_errors})
