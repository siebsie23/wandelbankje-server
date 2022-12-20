FROM python:3

ADD . /app/

RUN pip install -r /app/requirements.txt

CMD ["python", "-u", "/app/main.py"]