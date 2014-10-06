install:
	python setup.py install
bootstrap:
	./.bootstrap.sh
lint:
	flake8 ncsdaemon/
test: lint
	py.test --with-coverage --cover-package=ncsdaemon ncsdaemon/tests/
clean:
	find ncsdaemon/ -name *.pyc | xargs rm && \
	rm -rf build/ dist/ ncsdaemon.egg-info/
