from fastapi import APIRouter, status, File
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException
from ocr_app.utils.Helper import Helper
from ocr_app.models.Schemas import TessreactConfig
from ocr_app.utils.TesseractOCR import get_text_using_tesseract

router = APIRouter(prefix="/tesseract", tags=["tesseract"], responses={404: {"description": "Not found"}})


@router.post("/image_to_text/", status_code=status.HTTP_201_CREATED)
async def image_to_text(request: TessreactConfig):
    try:
        lobj_helper = Helper(request.input_file.file_name)
        lstr_input_file = lobj_helper.save_file_to_disk(request.input_file)
        lstr_output_file = get_text_using_tesseract(lstr_input_file, request.psm, request.oem, request.lang)
        lobj_helper.clean_disk()
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={"check": "success"})
    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(ex))
