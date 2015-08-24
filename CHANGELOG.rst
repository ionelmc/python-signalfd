
Changelog
=========

0.3.0 (2015-08-24)
------------------

* Corrected error handling in signalfd and sigprocmask wrappers.

0.2.0 (2015-08-24)
------------------

* Changed ``read_siginfo`` so it raises IOError in case is used with a file object and ``.readinto()`` would return ``None``
  (not enough data available).

0.1.0 (2015-08-23)
-----------------------------------------

* First release on PyPI.
