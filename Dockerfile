FROM python:3.10-alpine

ADD . /app/

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "-u", "/app/main.py"]