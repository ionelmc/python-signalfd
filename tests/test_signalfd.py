import errno
import os
import signal

import pytest

import signalfd


def test_block_and_read():
    fd = signalfd.signalfd(-1, [signal.SIGUSR1], signalfd.SFD_CLOEXEC)
    try:
        signalfd.sigprocmask(signalfd.SIG_BLOCK, [signal.SIGUSR1])
        os.kill(os.getpid(), signal.SIGUSR1)
        si = signalfd.read_siginfo(fd)
        assert si.ssi_signo == signal.SIGUSR1
    finally:
        os.close(fd)


def test_read_fd_no_data():
    fd = signalfd.signalfd(-1, [signal.SIGUSR1], signalfd.SFD_CLOEXEC | signalfd.SFD_NONBLOCK)
    try:
        err = pytest.raises((OSError, IOError), signalfd.read_siginfo, fd)
        assert err.value.errno == errno.EAGAIN
    finally:
        os.close(fd)


def test_read_fh_no_data():
    fd = signalfd.signalfd(-1, [signal.SIGUSR1], signalfd.SFD_CLOEXEC | signalfd.SFD_NONBLOCK)
    fh = os.fdopen(fd, 'rb')
    try:
        err = pytest.raises((OSError, IOError), signalfd.read_siginfo, fh)
        assert err.value.errno == errno.EAGAIN
    finally:
        fh.close()


def test_read_closed():
    fd = signalfd.signalfd(-1, [signal.SIGUSR1], signalfd.SFD_CLOEXEC)
    os.close(fd)
    pytest.raises(OSError, signalfd.read_siginfo, fd)


def test_invalid_fd():
    pytest.raises(ValueError, signalfd.signalfd, 0, [signal.SIGUSR1], signalfd.SFD_CLOEXEC)


def test_invalid_fd_2():
    pytest.raises(ValueError, signalfd.signalfd, 999999999, [signal.SIGUSR1], signalfd.SFD_CLOEXEC)


def test_invalid_flags_str():
    pytest.raises(TypeError, signalfd.signalfd, -1, [signal.SIGUSR1], 'sadfsadf')


def test_invalid_flags_float():
    pytest.raises(TypeError, signalfd.signalfd, -1, [signal.SIGUSR1], 1.2)


def test_invalid_signals():
    pytest.raises(TypeError, signalfd.signalfd, -1, 'fooo', 0)


def test_invalid_signals_noniterable():
    pytest.raises(TypeError, signalfd.signalfd, -1, object(), 0)


def test_invalid_flags():
    pytest.raises(ValueError, signalfd.signalfd, -1, [signal.SIGUSR1], 123123)
