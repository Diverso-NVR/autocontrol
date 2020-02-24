FROM python:3

ARG VERSION=1

COPY . /nvr_autocontrol

RUN pip install --no-cache-dir -r /nvr_autocontrol/requirements.txt

ENV PYTHONPATH /nvr_autocontrol

CMD ["python", "/nvr_autocontrol/app.py"]

