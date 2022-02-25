import mimetypes
import os.path
import shutil
import uuid
import base64

from ocr_app.core.configurations import TEMP_FOLDER_PATH
from ocr_app.models.Schemas import InputFile


class Helper:
    def __init__(self, pstr_base_folder_name: str = uuid.uuid4()):
        try:
            self.gstr_base_folder_path = os.path.join(str(TEMP_FOLDER_PATH), str(pstr_base_folder_name))
            if not os.path.exists(self.gstr_base_folder_path):
                os.makedirs(self.gstr_base_folder_path, exist_ok=True)

        except Exception:
            raise

    def save_file_to_disk(self, lobj_input_file: InputFile):
        lstr_file_path = None
        try:
            if lobj_input_file.__validate__():
                lstr_file_path = os.path.join(self.gstr_base_folder_path, str(lobj_input_file.file_name) +
                                              str(mimetypes.guess_extension(str(lobj_input_file.file_type))))
                with open(lstr_file_path, "wb") as lobj_file:
                    lobj_file.write(base64.b64decode(lobj_input_file.file_bytes))
        except Exception:
            raise
        return lstr_file_path

    def clean_disk(self):
        try:
            if os.path.exists(self.gstr_base_folder_path):
                shutil.rmtree(self.gstr_base_folder_path, ignore_errors=True)
        except Exception:
            raise
