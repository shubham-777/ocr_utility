FROM python:3.10.2
WORKDIR /app
COPY . .
RUN pip install -r ./requirements.txt
CMD ["python", "./ocr_app/main.py"]
EXPOSE 8000