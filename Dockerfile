FROM python:3

COPY ./autocontrol /autocontrol
COPY ./requirements.txt /

RUN pip install -r requirements.txt

CMD ["python", "/autocontrol/app.py"]

