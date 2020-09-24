FROM python:3

ARG VERSION=1

COPY ./autocontrol /autocontrol
COPY ./requirements.txt /

RUN pip install -r requirements.txt

ENV PYTHONPATH /autocontrol

CMD ["python", "/autocontrol/app.py"]

