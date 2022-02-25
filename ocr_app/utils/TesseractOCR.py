import os.path
import subprocess, shlex
import pandas as pd

lstr_tesseract = "tesseract"


def get_text_using_tesseract(pstr_image_path, pint_psm, pint_oem, pstr_lang):
    try:
        lstr_image_name, lstr_extension = os.path.splitext(os.path.basename(pstr_image_path))
        lstr_output_file_path = os.path.join(os.path.dirname(pstr_image_path), lstr_image_name)
        lstr_cmd = f"{lstr_tesseract} {pstr_image_path} {lstr_output_file_path} -l {pstr_lang} --oem {pint_oem} --psm {pint_psm} tsv"
        llst_command = lstr_cmd.split(" ")
        lobj_popen = subprocess.Popen(llst_command, stdout=subprocess.PIPE)
        while lobj_popen.poll() is None:
            pass
        if lobj_popen.poll() is not None and lobj_popen.poll() == 0:
            return lstr_output_file_path + ".tsv"
        else:
            raise Exception(f"Failed to run command {lstr_cmd} returned code {lobj_popen.poll()}")
    except Exception:
        raise


def prepare_result(pstr_tsv_file_path):
    try:
        df = pd.read_csv(pstr_tsv_file_path, sep='\t')
    except Exception:
        raise