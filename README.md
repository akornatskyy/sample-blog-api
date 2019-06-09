# Sample Blog API

[![Build Status](https://travis-ci.org/akornatskyy/sample-blog-api.svg?branch=master)](https://travis-ci.org/akornatskyy/sample-blog-api)
[![Code Climate](https://codeclimate.com/github/akornatskyy/sample-blog-api/badges/gpa.svg)](https://codeclimate.com/github/akornatskyy/sample-blog-api)

A simple blog API written using [python](http://python.org/) and
[wheezy.web](https://bitbucket.org/akorn/wheezy.web) framework.

# Setup

Virtual environment:

    virtualenv -p python2.7 env
    source env/bin/activate

on Windows:

	virtualenv.exe env
	env\Scripts\activate.bat

install dependencies:

    pip install -e .

install development dependencies:

    pip install -r requirements.txt

# Prepare

The static content in
[sample-blog-react](https://github.com/akornatskyy/sample-blog-react)
need to be build with *web* api strategy:

    cd ../sample-blog-react
    API=web npm run build

and linked to `content/static` directory:

    cd ../sample-blog-api
    ln -s ../../sample-blog-react/dist content/static

# Run

Serve files with paster (`pip install pastescript`) web server:

    paster serve --reload etc/development.ini

or uwsgi:

    uwsgi --ini etc/development.ini

or gunicorn:

    gunicorn -b 0.0.0.0:8080 -w 1 app:main

Open your browser at [http://localhost:8080](http://localhost:8080),
use *demo* / *password*.
