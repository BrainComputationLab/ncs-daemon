ncsdaemon
======================================
[![Build Status](https://travis-ci.org/BrainComputationLab/ncsdaemon.svg?branch=master)](https://travis-ci.org/BrainComputationLab/ncsdaemon)
[![Coverage Status](https://coveralls.io/repos/BrainComputationLab/ncsdaemon/badge.png?branch=master)](https://coveralls.io/r/BrainComputationLab/ncsdaemon?branch=master)
[![Documentation Status](https://readthedocs.org/projects/ncsdaemon/badge/?version=latest)](https://readthedocs.org/projects/ncsdaemon/?badge=latest)
[![PyPI version](https://badge.fury.io/py/ncsdaemon.svg)](http://badge.fury.io/py/ncsdaemon)

A service running on a master node that allows clients to interact with the NCS brain simulator using a restful API.

Development
--------------------------------------

Install the latest version by cloning the repository.

~~~
git clone https://github.com/BrainComputationLab/ncsdaemon.git
~~~

Bootstrap your development environment.

~~~
make bootstrap
~~~

Activate your virtualenv.

~~~
source env/bin/activate
~~~

Run Tests.

~~~
make test
~~~

Happy developing!
