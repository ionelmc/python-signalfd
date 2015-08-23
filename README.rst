========
signalfd
========

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |coveralls| |codecov|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/python-signalfd/badge/?style=flat
    :target: https://readthedocs.org/projects/python-signalfd
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/ionelmc/python-signalfd.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/python-signalfd

.. |requires| image:: https://requires.io/github/ionelmc/python-signalfd/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/ionelmc/python-signalfd/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/ionelmc/python-signalfd/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/ionelmc/python-signalfd

.. |codecov| image:: https://codecov.io/github/ionelmc/python-signalfd/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/ionelmc/python-signalfd

.. |version| image:: https://img.shields.io/pypi/v/signalfd.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/signalfd

.. |downloads| image:: https://img.shields.io/pypi/dm/signalfd.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/signalfd

.. |wheel| image:: https://img.shields.io/pypi/wheel/signalfd.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/signalfd

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/signalfd.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/signalfd

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/signalfd.svg?style=flat
    :alt: Supported imlementations
    :target: https://pypi.python.org/pypi/signalfd

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
