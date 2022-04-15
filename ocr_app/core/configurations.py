import configparser
import os

package_path, package_filename = os.path.split(os.path.abspath(__file__))
config = configparser.ConfigParser()
config.read(os.path.join(package_path, "data/config.ini"))

PACKAGE_PATH = package_path

TEMP_FOLDER_NAME = str(config["PATHS"]["TEMP_FOLDER_NAME"])
TEMP_FOLDER_PATH = os.path.join(PACKAGE_PATH, TEMP_FOLDER_NAME)
HOST = str(config["ENVIRONMENT"]["HOST"])
PORT = int(config["ENVIRONMENT"]["PORT"])
PRODUCTION_MODE = eval(config["ENVIRONMENT"]["PRODUCTION_MODE"])
APPIMAGE_510_PATH = str(config["TESSERACT"]["APPIMAGE_510_PATH"])
