"""
Simple wrapper around the signalfd syscall.
"""

import errno
import os
import signal

from ._signalfd import ffi as _ffi
from ._signalfd import lib as _lib

__version__ = '1.0.0'

SFD_CLOEXEC = _lib.SFD_CLOEXEC
SFD_NONBLOCK = _lib.SFD_NONBLOCK

SIG_BLOCK = _lib.SIG_BLOCK
SIG_UNBLOCK = _lib.SIG_UNBLOCK
SIG_SETMASK = _lib.SIG_SETMASK

SIGINFO_SIZE = _ffi.sizeof('struct signalfd_siginfo')
ALL_SIGNALS = sorted(getattr(signal, s) for s in dir(signal) if s.startswith('SIG') and '_' not in s)


class UnknownError(Exception):
    pass


def signalfd(fd, signals, flags):
    if hasattr(fd, 'fileno'):
        fd = fd.fileno()

    if not isinstance(fd, int):
        raise TypeError('fd: must be an integer.')
    if not isinstance(flags, int):
        raise TypeError('flags: must be an integer.')

    sigmask = _ffi.new('sigset_t[1]')
    for sig in signals:
        _lib.sigaddset(sigmask, sig)

    result = _lib.signalfd(fd, sigmask, flags)

    if result < 0:
        err = _ffi.errno
        if err == errno.EBADF:
            raise ValueError('fd: not a valid file descriptor.')
        elif err == errno.EINVAL:
            if flags & (0xFFFFFFFF ^ (SFD_CLOEXEC | SFD_NONBLOCK)):
                raise ValueError('flags: mask contains invalid values.')
            else:
                raise ValueError('fd: not a signalfd.')
        elif err == errno.EMFILE:
            raise OSError('max system fd limit reached.')
        elif err == errno.ENFILE:
            raise OSError('max system fd limit reached.')
        elif err == errno.ENODEV:
            raise OSError('could not mount (internal) anonymous inode device.')
        elif err == errno.ENOMEM:
            raise MemoryError('insufficient kernel memory available.')
        else:
            raise UnknownError(err)

    return result


def sigprocmask(flags, signals):
    if not isinstance(flags, int):
        raise TypeError('flags: must be an integer.')

    new_sigmask = _ffi.new('sigset_t[1]')
    old_sigmask = _ffi.new('sigset_t[1]')

    _lib.sigemptyset(new_sigmask)
    for sig in signals:
        _lib.sigaddset(new_sigmask, sig)

    err = _lib.pthread_sigmask(flags, new_sigmask, old_sigmask)

    if err:
        if err == errno.EINVAL:
            raise ValueError('flags: invalid value (not one of SIG_BLOCK, SIG_UNBLOCK or SIG_SETMASK)')
        elif err == errno.EFAULT:
            raise ValueError('sigmask is not a valid sigset_t')
        else:
            raise UnknownError(err)

    return [s for s in ALL_SIGNALS if _lib.sigismember(old_sigmask, s)]


def read_siginfo(fh):
    info = _ffi.new('struct signalfd_siginfo *')
    buffer = _ffi.buffer(info)

    if hasattr(fh, 'readinto'):
        if not fh.readinto(buffer):
            raise OSError(errno.EAGAIN, 'not enough bytes available')
    else:
        buffer[:] = os.read(fh, SIGINFO_SIZE)
    return info
