.SILENT: install test qa run paster uwsgi gunicorn clean release
.PHONY: install test qa run paster uwsgi gunicorn clean release

all: test qa

install:
	pip install -e . -r requirements.txt

test:
	pytest -q -x --pep8 --doctest-modules src/

qa:
	flake8 --max-complexity 6 src setup.py \
		&& pep8 src setup.py

run:
	python -m app

paster:
	paster serve --reload etc/development.ini

uwsgi:
	uwsgi --ini etc/development.ini

gunicorn:
	gunicorn -b 0.0.0.0:8080 -w 1 app:main

clean:
	find src/ -type d -name __pycache__ | xargs rm -rf \
		&& find src/ -name '*.py[co]' -delete \
		&& find src/ -name '*.cache' -delete \
		&& rm -rf .cache .coverage src/*.egg-info/ build/ dist/

release:
	rm -rf src/*.egg-info/ \
		&& REV=$$(git rev-list --count HEAD) \
		&& python setup.py -q egg_info --tag-build .$$REV sdist \
		&& NAME=$$(python setup.py --fullname).$$REV \
		&& rm -rf dist/$$NAME \
		&& tar xzf dist/$$NAME.tar.gz -C dist/ \
		&& rm dist/$$NAME.tar.gz \
		&& sed -i'' "s/, 0)/, $$REV)/" dist/$$NAME/src/public/__init__.py \
		&& python -OO -m compileall -q dist/$$NAME/src \
		&& tar cf - -C dist/ $$NAME | gzip -9 - > dist/$$NAME.tar.gz \
		&& rm -rf dist/$$NAME
