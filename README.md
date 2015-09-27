# Sample Blog API

[![Code Climate](https://codeclimate.com/github/akornatskyy/sample-blog-api/badges/gpa.svg)](https://codeclimate.com/github/akornatskyy/sample-blog-api)

A simple blog API written using [python](http://python.org/) and
[wheezy.web](https://bitbucket.org/akorn/wheezy.web) framework.

# Setup

Install dependencies into virtual environment:

    virtualenv --python=/opt/local/bin/python2.7 env
    source env/bin/activate
    python setup.py develop
    easy_install pastescript

# Prepare

The static content in
[sample-blog-react](https://github.com/akornatskyy/sample-blog-react)
need to be build with *web* api strategy:

    cd ../sample-blog-react
    gulp build --api=web

optionally:

    gulp watch --debug --api=web

and linked to `content/static` directory:

    cd ../sample-blog-api
    ln -s ../../sample-blog-react/build content/static

# Run

Serve files with a web server:

    paster serve --reload etc/development.ini

Open your browser at [http://localhost:8080](http://localhost:8080),
use *demo* / *password*.
