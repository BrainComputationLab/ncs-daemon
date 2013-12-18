""" ncsdaemon setup script """

from setuptools import setup, find_packages

setup(
    name='ncsdaemon',
    version='0.01a',
    url='http://github.com/braincomputationlab/ncs-daemon',
    license='MIT',
    author='Nathan Jordan',
    author_email='natedagreat27274@gmail.com',
    description='A service running on a master node that allows clients to interact with the NCS brain simulator using a restful API',
    long_description=open('README.rst').read() + '\n\n' + open('CHANGELOG.rst').read(),
    packages=find_packages(exclude=['tests']),
    install_requires=['flask', 'flask-restful', 'jsonschema'],
    entry_points={
        'console_scripts': [
            'ncsdaemon = ncsdaemon.console:console_main'
        ]
    },
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
)
