import signal

import pytest

import signalfd


def test_invalid_flags_str():
    pytest.raises(TypeError, signalfd.sigprocmask, 'sadfsadf', [signal.SIGUSR1])


def test_invalid_flags_float():
    pytest.raises(TypeError, signalfd.sigprocmask, 1.2, [signal.SIGUSR1])


def test_invalid_signals():
    pytest.raises(TypeError, signalfd.sigprocmask, 0, 'foo')


def test_invalid_signals_noniterable():
    pytest.raises(TypeError, signalfd.sigprocmask, 0, object())


def test_invalid_flags():
    pytest.raises(ValueError, signalfd.sigprocmask, 3, [signal.SIGUSR1])


def test_block():
    signalfd.sigprocmask(signalfd.SIG_UNBLOCK, signalfd.ALL_SIGNALS)
    assert signalfd.sigprocmask(signalfd.SIG_BLOCK, [signal.SIGUSR1]) == []
    assert signalfd.sigprocmask(signalfd.SIG_BLOCK, [signal.SIGUSR2]) == [signal.SIGUSR1]
    assert signalfd.sigprocmask(signalfd.SIG_BLOCK, []) == [signal.SIGUSR1, signal.SIGUSR2]


def test_mask():
    signalfd.sigprocmask(signalfd.SIG_UNBLOCK, signalfd.ALL_SIGNALS)
    assert signalfd.sigprocmask(signalfd.SIG_SETMASK, [signal.SIGUSR1]) == []
    assert signalfd.sigprocmask(signalfd.SIG_SETMASK, [signal.SIGUSR2]) == [signal.SIGUSR1]
    assert signalfd.sigprocmask(signalfd.SIG_SETMASK, []) == [signal.SIGUSR2]
    assert signalfd.sigprocmask(signalfd.SIG_SETMASK, []) == []
