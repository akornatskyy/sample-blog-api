FROM python:2-alpine

MAINTAINER Andriy Kornatskyy <andriy.kornatskyy@live.com>

ENV PYTHON_EGG_CACHE /tmp

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
        git \
    \
    && git clone --depth=1 https://github.com/akornatskyy/sample-blog-api.git /app \
    \
    && cd /app \
    && python setup.py develop -O2 -U -Z \
    && easy_install -O2 -Z uwsgi \
    && chmod -R +r /usr/local/lib/python* \
    \
    && python -OO -m compileall src/ \
    && find src/ -name '*.py' -delete \
    \
    && apk del .build-deps

WORKDIR /app

COPY config.ini etc/

EXPOSE 8080

CMD uwsgi --ini etc/config.ini
