================
Scrapy-Pipelines
================

Overview
========

.. image:: https://bestpractices.coreinfrastructure.org/projects/2828/badge
   :alt: CII Best Practices
   :target: https://bestpractices.coreinfrastructure.org/projects/2828

.. image:: https://mperlet.github.io/pybadge/badges/9.43.svg
   :alt: pylint Score

.. image:: https://img.shields.io/travis/scrapedia/scrapy-pipelines/master.svg
   :target: http://travis-ci.org/scrapedia/scrapy-pipelines
   :alt: Travis branch

.. image:: https://codecov.io/gh/scrapedia/scrapy-pipelines/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/scrapedia/scrapy-pipelines
   :alt: Coverage Report

.. image:: https://codebeat.co/badges/fabc61ba-6a20-4bd1-bf73-a2f091a9ad80
   :target: https://codebeat.co/projects/github-com-scrapedia-scrapy-pipelines-master
   :alt: codebeat badge

.. image:: https://api.codacy.com/project/badge/Grade/aeda92e058434a9eb2e8b0512a02235f
   :target: https://www.codacy.com/app/grammy-jiang/scrapy-pipelines?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=scrapedia/scrapy-pipelines&amp;utm_campaign=Badge_Grade

.. image:: https://pyup.io/repos/github/scrapedia/scrapy-pipelines/shield.svg
     :target: https://pyup.io/repos/github/scrapedia/scrapy-pipelines/
     :alt: Updates

.. image:: https://snyk.io/test/github/scrapedia/scrapy-pipelines/badge.svg
    :target: https://snyk.io/test/github/scrapedia/scrapy-pipelines
    :alt: Known Vulnerabilities
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/python/black
    :alt: Code style: black

.. image:: https://img.shields.io/badge/License-GPLv3-blue.svg
    :target: https://www.gnu.org/licenses/gpl-3.0
    :alt: License: AGPL v3
    
These pipelines enable Scrapy to save items into various backends, including:

* MongoDB

And also these pipelines provide multiple ways to save or update the items, and
return id created by backends

Requirements
=============

.. image:: https://pyup.io/repos/github/scrapedia/r18/python-3-shield.svg
   :target: https://pyup.io/repos/github/scrapedia/r18/
   :alt: Python 3

* Python 3.6+
* Works on Linux, Windows, Mac OSX

Installation
============

.. image:: https://img.shields.io/pypi/v/scrapy-pipelines.svg
   :target: https://pypi.python.org/pypi/scrapy-pipelines
   :alt: PyPI
.. image:: https://img.shields.io/pypi/pyversions/scrapy-pipelines.svg
   :target: https://pypi.python.org/pypi/scrapy-pipelines
   :alt: PyPI - Python Version
.. image:: https://img.shields.io/pypi/wheel/scrapy-pipelines.svg
   :target: https://pypi.python.org/pypi/scrapy-pipelines
   :alt: PyPI - Wheel

The quick way:

   pip install scrapy-pipelines

For more details see the installation section in the documentation:
https://scrapy-pipelines.readthedocs.io/en/latest/intro/installation.html

Documentation
=============

Documentation is available online at
https://scrapy-pipelines.readthedocs.io/en/latest/ and in the docs directory.

Community (blog, twitter, mail list, IRC)
=========================================

*Keeping this section same as Scrapy is intending to benefit back to Scrapy.*

See https://scrapy.org/community/

Contributing
============

*Keeping this section same as Scrapy is intending to be easier when this repo
merge back to Scrapy.*

See https://doc.scrapy.org/en/master/contributing.html

Code of Conduct
---------------

Please note that this project is released with a Contributor Code of Conduct
(see https://github.com/scrapy/scrapy/blob/master/CODE_OF_CONDUCT.md).

By participating in this project you agree to abide by its terms.
Please report unacceptable behavior to opensource@scrapinghub.com.


Companies using Scrapy
======================

*Keeping this section same as Scrapy is intending to benefit back to Scrapy.*

See https://scrapy.org/companies/

Commercial Support
==================

*Keeping this section same as Scrapy is intending to benefit back to Scrapy.*

See https://scrapy.org/support/

TODO
====

* [X] Add indexes creation in open_spider()
* [X] Add item_completed method
* [X] Add signals for MongoDB document's id return
* [ ] Add MongoDB document update
* [ ] Add Percona Server for MongoDB docker support
* [ ] Add Redis support
* [ ] Add InfluxDB support
* [ ] Add LevelDB support
