"""
Python package configuration
"""
from setuptools import find_packages, setup

import versioneer

extras_require = {}

with open("README.rst", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name="Scrapy-Pipelines",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url="https://github.com/scrapedia/scrapy-pipelines",
    description="A collection of scrapy item pipelines",
    long_description=LONG_DESCRIPTION,
    author="Scrapedia",
    author_email="Scrapedia@outlook.com",
    maintainer="Scrapedia",
    maintainer_email="Scrapedia@outlook.com",
    license="GPLv3",
    packages=find_packages(exclude=("tests", "tests.*")),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Framework :: Scrapy",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=["scrapy", "txmongo"],
    extras_require=extras_require,
)
