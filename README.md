# OCR Utility using FastAPI

ocr_utility is a ocr comparision utility for developers.

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
│       ├── TesseractOCR.py
│       └── __init__.py
├── README.md
└── requirement.txt
```
## Requirements:

1. Python 3.6+
2. pip modules in requirements.txt

### Installation command for pip modules:

```sh
pip install -r .\requirement.txt
```