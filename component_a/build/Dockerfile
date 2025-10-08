# Refer to README.md for commonly used PyTorch images
FROM python:3.12.11-slim-bookworm

ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

ENV DEBIAN_FRONTEND noninteractive
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /build
WORKDIR /build

ADD build/requirements.txt /build/requirements.txt
RUN pip install --no-cache-dir --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt

ADD src/ /workspace/src

WORKDIR /workspace/src

CMD python main.py