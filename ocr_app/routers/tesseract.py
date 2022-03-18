"""
Router for tesseract.
"""
from fastapi import APIRouter, UploadFile
from utils import tesseract as tesseract_helper
router = APIRouter(prefix="/tesseract",
                   tags=["tesseract"])


@router.get("/supported_formats/")
async def get_supported_formats():
    """
    return supported file formats by the current version of the api.
    """
    try:
        return tesseract_helper.SUPPORTED_TYPES
    except Exception:
        print(str(Exception))
        raise


@router.post("/image_to_text/")
async def image_to_text(file: UploadFile):
    """
    return ocr json generated by tesseract for given input.
    """
    try:
        await file.read()
        tesseract_helper.validate_file_type(file)
        return {"text": "lorem ipsum"}
    except Exception:
        print(str(Exception))
        raise
    # try:
    #     lobj_helper = Helper(request.input_file.file_name)
    #     lstr_input_file = lobj_helper.save_file_to_disk(request.input_file)
    #     lstr_output_file = get_text_using_tesseract(
    #         lstr_input_file, request.psm, request.oem, request.lang)
    #     lobj_helper.clean_disk()
    #     return JSONResponse(status_code=status.HTTP_201_CREATED, content={"check": "success"})
    # except Exception as ex:
    #     raise HTTPException(
    #         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(ex))
