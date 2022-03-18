"""
python file containing all helper functions needed for tesseract functions.
"""
from fastapi import HTTPException, status
SUPPORTED_TYPES = [
    {"title": "Bitmap Image File",
     "file_extension": ["bmp", "dib"],
     "media_type": ["image/bmp", "image/x-bmp"]},
    {"title": "Portable Anymap Format",
     "file_extension": ["pbm", "pgm", "ppm", "pnm"],
     "media_type": ["image/x-portable-bitmap", "image/x-portable-graymap",
                    "image/x-portable-pixmap", "image/x-portable-anymap"]},
    {"title": "Portable Network Graphics",
     "file_extension": ["png"],
     "media_type": ["image/png"]},
    {"title": "Joint Photographic Experts Group",
     "file_extension": ["jpg", "jpeg", "jpe", "jif", "jfif", "jfi"],
     "media_type": ["image/jpeg"]},
    {"title": "Tag Image File Format",
     "file_extension": ["tiff", "tif"],
     "media_type": ["image/tiff", "image/tiff-fx"]}
]

SUPPORTED_MEDIA_TYPES = []
for item in [x["media_type"] for x in SUPPORTED_TYPES]:
    SUPPORTED_MEDIA_TYPES.extend(item)

SUPPORTED_FILE_EXTENSIONS = []
for item in [x["file_extension"] for x in SUPPORTED_TYPES]:
    SUPPORTED_FILE_EXTENSIONS.extend(item)


def validate_file_type(upload_file_obj):
    """
    Utility function to validate the file type and extension.
    """
    file_extension = upload_file_obj.filename.split(".")[-1]
    if not (upload_file_obj.content_type.lower() in SUPPORTED_MEDIA_TYPES and file_extension.lower() in SUPPORTED_FILE_EXTENSIONS):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="File type not supported. Check supported file formats by sending a get request to /tesseract/supported_formats/.")
# import os.path
# import subprocess, shlex
# import pandas as pd

# lstr_tesseract = "tesseract"


# def get_text_using_tesseract(pstr_image_path, pint_psm, pint_oem, pstr_lang):
#     try:
#         lstr_image_name, lstr_extension = os.path.splitext(os.path.basename(pstr_image_path))
#         lstr_output_file_path = os.path.join(os.path.dirname(pstr_image_path), lstr_image_name)
#         lstr_cmd = f"{lstr_tesseract} {pstr_image_path} {lstr_output_file_path} -l {pstr_lang} --oem {pint_oem} --psm {pint_psm} tsv"
#         llst_command = lstr_cmd.split(" ")
#         lobj_popen = subprocess.Popen(llst_command, stdout=subprocess.PIPE)
#         while lobj_popen.poll() is None:
#             pass
#         if lobj_popen.poll() is not None and lobj_popen.poll() == 0:
#             return lstr_output_file_path + ".tsv"
#         else:
#             raise Exception(f"Failed to run command {lstr_cmd} returned code {lobj_popen.poll()}")
#     except Exception:
#         raise


# def prepare_result(pstr_tsv_file_path):
#     try:
#         df = pd.read_csv(pstr_tsv_file_path, sep='\t')
#     except Exception:
#         raise
