FROM python:3
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /
WORKDIR /app
