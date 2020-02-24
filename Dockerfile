FROM python:3

ARG VERSION=1

COPY . /autocontrol

RUN pip install --no-cache-dir -r /autocontrol/requirements.txt

ENV PYTHONPATH /autocontrol

CMD ["python", "/autocontrol/app.py"]

