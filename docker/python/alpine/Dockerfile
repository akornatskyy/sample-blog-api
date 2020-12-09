FROM python:3-alpine

MAINTAINER Andriy Kornatskyy <andriy.kornatskyy@live.com>

RUN set -ex \
    \
    && addgroup -S www-data \
    && adduser -D -S -h /app -s /sbin/nologin -G www-data www-data \
    \
    && apk add --no-cache \
        pcre \
    \
    && apk add --no-cache --virtual .build-deps \
        musl-dev \
        linux-headers \
        pcre-dev \
        gcc \
        g++ \
        git \
    \
    && git clone --depth=1 https://github.com/akornatskyy/sample-blog-api.git /app \
    \
    && cd /app \
    && pip --no-cache-dir install -e . uwsgi \
    \
    && python -OO -m compileall src/ \
    \
    && apk del .build-deps

WORKDIR /app

COPY config.ini etc/

EXPOSE 8080

CMD uwsgi --ini etc/config.ini
