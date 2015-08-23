import os
import signal

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
