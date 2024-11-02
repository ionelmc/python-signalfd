========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |github-actions| |coveralls| |codecov|
    * - package
      - |version| |wheel| |supported-versions| |supported-implementations| |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-signalfd/badge/?style=flat
    :target: https://readthedocs.org/projects/python-signalfd/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/ionelmc/python-signalfd/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/ionelmc/python-signalfd/actions

.. |coveralls| image:: https://coveralls.io/repos/github/ionelmc/python-signalfd/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://coveralls.io/github/ionelmc/python-signalfd?branch=master

.. |codecov| image:: https://codecov.io/gh/ionelmc/python-signalfd/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://app.codecov.io/github/ionelmc/python-signalfd

.. |version| image:: https://img.shields.io/pypi/v/signalfd.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/signalfd

.. |wheel| image:: https://img.shields.io/pypi/wheel/signalfd.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/signalfd

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/signalfd.svg
    :alt: Supported versions
    :target: https://pypi.org/project/signalfd

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/signalfd.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/signalfd

.. |commits-since| image:: https://img.shields.io/github/commits-since/ionelmc/python-signalfd/v1.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/ionelmc/python-signalfd/compare/v1.0.0...master

.. end-badges

CFFI bindings for signalfd. Interface is mostly the same as https://pypi.python.org/pypi/python-signalfd

* Free software: BSD license

Installation
============

::

    pip install signalfd

Usage
=====

.. sourcecode:: python

    import signalfd

    fd = signalfd.signalfd(-1, [signal.SIGUSR1], signalfd.SFD_CLOEXEC)
    try:
        signalfd.sigprocmask(signalfd.SIG_BLOCK, [signal.SIGUSR1])

        while True:
            si = signalfd.read_siginfo(fd)
            print(si.ssi_signo)
    finally:
        os.close(fd)


Documentation
=============

https://python-signalfd.readthedocs.org/

Development
===========

To run the all tests run::

    tox
