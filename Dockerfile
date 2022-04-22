FROM python:3.10.2
WORKDIR /app
COPY . .
RUN pip install -r ./requirements.txt
EXPOSE $PORT
CMD ["python", "./ocr_app/main.py"]
