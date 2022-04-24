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
- Toggle the PRODUCTION_MODE variable in config before pushing to production.

### Command to install all requirements (virtual environment recommended):

```sh
pip install -r .\requirements.txt
```

### Command to run the app:

```sh
python ./ocr_app/main.py
```

### Command to build the docker image:

```sh
docker build -t ocr_utility .
```

### Command to run the docker image:

```sh
docker run -p 8000:8000 ocr_utility
```

### Command to push the docker image to heroku

```sh
heroku container:push web -a ocr_utility
heroku container:release web -a ocr_utility
```
