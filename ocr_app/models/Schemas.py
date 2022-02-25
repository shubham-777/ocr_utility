import mimetypes

from fastapi import File
from pydantic import BaseModel


class InputFile(BaseModel):
    file_bytes: str
    file_name: str
    file_type: str

    def __repr__(self):
        return vars(self)

    def __validate__(self):
        if self.file_name is not None and self.file_type is not None and self.file_bytes is not None:
            return True
        else:
            return False


class TessreactConfig(BaseModel):
    input_file: InputFile
    psm: int
    oem: int
    lang: str

    def __repr__(self):
        return {"input_file": self.input_file.__repr__(), "psm": self.psm, "oem": self.oem, "land": self.lang}

    def __validate__(self):
        if self.input_file.__validate__() and 0 <= self.psm <= 13 and 0 <= self.oem <= 3 and self.lang is not None:
            return True
        else:
            return False
