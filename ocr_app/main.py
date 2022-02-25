import os
import uvicorn
import mimetypes
from fastapi import FastAPI, Request, status, Response
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exception_handlers import http_exception_handler

from routers import tesseract

author = "Shubham Ahinave"

app = FastAPI(title="OCR",
              version="1.0.0",
              contact={
                  "name": "Shubham Ahinave",
                  "url": "https://github.com/shubham-777",
                  "email": "codesign.developers@gmail.com",
              })


@app.get("/", status_code=200)
def root(request: Response):
    return JSONResponse(status_code=status.HTTP_200_OK, content={"health": "success"})


app.include_router(tesseract.router)


@app.exception_handler(StarletteHTTPException)
async def my_custom_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=exc.detail)
    else:
        # Just use FastAPI's built-in handler for other errors
        return await http_exception_handler(request, exc)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
