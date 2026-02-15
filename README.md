# Sample Blog API

[![tests](https://github.com/akornatskyy/sample-blog-api/actions/workflows/tests.yml/badge.svg)](https://github.com/akornatskyy/sample-blog-api/actions/workflows/tests.yml)

A simple blog API written using [python](http://python.org/) and
[wheezy.web](https://bitbucket.org/akorn/wheezy.web) framework.

## Setup

Virtual environment:

```sh
py -mvenv env
. env/bin/activate
```

install dependencies:

```sh
pip install -e .
```

install development dependencies:

```sh
pip install -r requirements/dev.txt
```

## Prepare

The static content in
[sample-blog-react](https://github.com/akornatskyy/sample-blog-react)
need to be build with *web* api strategy:

```sh
cd ../sample-blog-react
API=web npm run build
```

and linked to `content/static` directory:

```sh
cd ../sample-blog-api
ln -s ../../sample-blog-react/dist content/static
```

## Run

Serve with:

```sh
python src/app
```

or uwsgi:

```sh
uwsgi --ini etc/development.ini
```

or gunicorn:

```sh
gunicorn -b 0.0.0.0:8080 -w 1 app:main
```

Open your browser at [http://localhost:8080](http://localhost:8080),
use *demo* / *password*.
