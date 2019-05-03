FROM alpine:3.5

MAINTAINER Sergey Burenko <sburenko86@gmail.com>

RUN apk add --no-cache python3 && python3 -m ensurepip && rm -r /usr/lib/python*/ensurepip && pip3 install --upgrade pip setuptools && rm -r /root/.cache

RUN apk add --update build-base vim curl bash zip git linux-headers python3-dev py-psutil && rm -rf /var/cache/apk/*
