#python:3.8.2
# FROM python@sha256:0ad49c7aa9e0a4139decace2b59905fa5b835b8c0c771ae7589eef03824bb8e9
FROM python@sha256:b45f6421a289f9cb33457ca17adb226d904823c719b6c744be97b7dedefa485b
FROM python:3.7 AS builder
WORKDIR /app

ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --timeout 60 -r requirements.txt

COPY ./ ./

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "-w", "1", "app:server_app"]
