from __future__ import absolute_import, unicode_literals
from setuptools import setup, find_packages

setup(
    name="ncsdaemon",
    version="0.01a",
    url="http://github.com/braincomputationlab/ncs-daemon",
    license="MIT",
    author="Nathan Jordan",
    author_email="nathan.m.jordan@gmail.com",
    description=("A service running on a master node that allows clients to"
                 "interact with the NCS brain simulator using a restful API"),
    long_description=(
        open("README.md").read() +
        "\n\n" +
        open("CHANGELOG.md").read()),
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
    ],
    entry_points="""
        [console_scripts]
        ncsdaemon=ncsdaemon.app:run
    """,
)
