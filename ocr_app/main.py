"""
Main file for the ocr_utility.
"""
import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.tesseract import router
from core.configurations import HOST, PORT, PRODUCTION_MODE
AUTHOR = "Shubham Ahinave"

app = FastAPI(title="ocr_utility",
              version="1.0.0",
              contact={
                  "name": "Shubham Ahinave",
                  "url": "https://github.com/shubham-777",
                  "email": "codesign.developers@gmail.com",
              })
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)


@app.get("/")
async def root():
    """
    root function for ocr_utility.
    """
    return {"message": "ocr_utility"}


if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=os.environ.get(
        'PORT', PORT), reload=(not PRODUCTION_MODE))
