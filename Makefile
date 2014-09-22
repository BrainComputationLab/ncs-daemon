install:
	python setup.py install
bootstrap:
	./.bootstrap.sh
lint:
	flake8 ncsdaemon/
test: lint
	py.test --with-coverage --cover-package=ncsdaemon ncsdaemon/tests/