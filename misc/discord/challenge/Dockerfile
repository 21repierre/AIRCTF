FROM python:3.9-slim-buster

COPY src/ /app

RUN pip3 install -r /app/requirements.txt

CMD ["python3", "/app/main.py"]
