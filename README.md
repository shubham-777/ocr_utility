# ocr_utility using FastAPI

ocr_utility is a ocr comparision utility.

## Project Structure

```
.
├── ocr_app
│   ├── __init__.py
│   ├── main.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── configurations.py
│   │   └── data
│   │       └── config.ini
│   ├── models
│   │   ├── Schemas.py
│   │   └── __init__.py
│   ├── routers
│   │   ├── __init__.py
│   │   └── tesseract.py
│   └── utils
│       ├── Helper.py
│       ├── tesseract.py
│       └── __init__.py
├── README.md
└── requirement.txt
```

## Notes:

- Tested on Python 3.10.2

### Command to install all requirements (virtual environment recommended):

```sh
pip install -r .\requirements.txt
```

### Command to run the app:

```sh
python ./ocr_app/main.py
```
