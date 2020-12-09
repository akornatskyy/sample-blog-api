FROM pypy:3-slim

MAINTAINER Andriy Kornatskyy <andriy.kornatskyy@live.com>

RUN set -ex \
    \
    && buildDeps=' \
      git \
      build-essential \
    ' \
    && apt-get update \
    && apt-get -y upgrade \
    && apt-get install -y $buildDeps --no-install-recommends \
    \
    && git clone --depth=1 https://github.com/akornatskyy/sample-blog-api.git /app \
    \
    && cd /app \
    && mkdir -p content/static/css content/static/js \
    && pip --no-cache-dir install -e . gunicorn \
    \
    && pypy3 -OO -m compileall src/ \
    \
    && apt-get purge -y --auto-remove $buildDeps \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

EXPOSE 8080

CMD gunicorn -b :8080 -w 1 app:main
