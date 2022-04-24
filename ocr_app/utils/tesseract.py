"""
python file containing all helper functions needed for tesseract functions.
"""
import os
import json
import subprocess
from unittest import result
import uuid
import pandas as pd
from fastapi import HTTPException, status
from core.configurations import TEMP_FOLDER_PATH, PRODUCTION_MODE, APPIMAGE_510_PATH

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
    if not (upload_file_obj.content_type.lower() in SUPPORTED_MEDIA_TYPES and
            file_extension.lower() in SUPPORTED_FILE_EXTENSIONS):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="File type not supported. Check" +
            " supported file formats by sending a get request to /tesseract/supported_formats/.")


def download_file(upload_file_obj, contents):
    """
    Utility function to download the file from the request.
    """
    try:
        file_path = file_path = os.path.join(
            TEMP_FOLDER_PATH, str(uuid.uuid4()) + "." + upload_file_obj.filename.split(".")[-1])
        with open(file_path, "wb") as file:
            file.write(contents)
        return file_path
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to download file. Error: {e}")


def image_to_text(file_path, pint_psm=3, pint_oem=1, pstr_lang="eng"):
    """
     Utility function to run the tesseract command on the terminal.
    """
    try:
        output_path = f"{file_path.split('.')[0]}-output"
        if PRODUCTION_MODE:
            llst_command = [APPIMAGE_510_PATH, "--appimage-extract-and-run", file_path,
                            output_path, "-l", pstr_lang, "--oem", str(
                                pint_oem), "--psm", str(pint_psm), "tsv"]
        else:
            llst_command = ["tesseract", file_path, output_path,
                            "-l", pstr_lang, "--oem", str(pint_oem),
                            "--psm", str(pint_psm), "tsv"]

        lobj_popen = subprocess.Popen(llst_command, stdout=subprocess.PIPE)
        while lobj_popen.poll() is None:
            pass
        if lobj_popen.poll() is not None and lobj_popen.poll() == 0:
            try:
                result = convert_tsv_to_json(output_path + ".tsv")
                return result, output_path + ".tsv"
            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"Failed to convert tsv to json. Error: {e}")
        else:
            raise Exception()
    except Exception:
        delete_files([output_path + ".tsv"])
        command = " ".join(llst_command)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to run {command} command. Returned code: {lobj_popen.poll()}")


def delete_files(file_paths):
    """
    Utility function to delete the files.
    """
    try:
        for file_path in file_paths:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Deleted {file_path}")
    except Exception:
        raise


def convert_tsv_to_json(file_path):
    result = {"pages": []}
    try:
        df = pd.read_csv(file_path, sep='\t').fillna('')
        for page_num in df["page_num"].unique():
            result["pages"].append({"page_num": int(page_num), "blocks": []})
            df_page = df[df["page_num"] == page_num]
            for block_num in df_page["block_num"].unique():
                result["pages"][-1]["blocks"].append(
                    {"block_num": int(block_num), "paragraphs": []})
                df_block = df_page[df_page["block_num"] == block_num]
                for par_num in df_block["par_num"].unique():
                    result["pages"][-1]["blocks"][-1]["paragraphs"].append(
                        {"par_num": int(par_num), "lines": []})
                    df_paragraph = df_block[df_block["par_num"]
                                            == par_num]
                    for line_num in df_paragraph["line_num"].unique():
                        result["pages"][-1]["blocks"][-1]["paragraphs"][-1]["lines"].append(
                            {"line_num": int(line_num), "words": []})
                        df_line = df_paragraph[df_paragraph["line_num"]
                                               == line_num]
                        for word_num in df_line["word_num"].unique():
                            for _, row in df_line[df_line["word_num"]
                                                  == word_num].iterrows():
                                result["pages"][-1]["blocks"][-1]["paragraphs"][-1]["lines"][-1]["words"].append(
                                    {"word_num": int(word_num), "text": row["text"], "top": float(row["top"]), "left": float(row["left"]), "width": float(row["width"]), "height": float(row["height"]), "conf": float(row["conf"])})
        return result
    except Exception:
        raise
