"""Daemon Module.
"""

import os
import sys


def daemonize() -> None:
    fork_and_exit_parent()
    os.chdir("/")
    os.setsid()
    fork_and_exit_parent()

    sys.stdout.flush()
    sys.stderr.flush()
    si = open(os.devnull, "r")
    so = open(os.devnull, "a+")
    se = open(os.devnull, "a+")
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())

    # while True: ...


def fork_and_exit_parent() -> None:
    try:
        pid: int = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError as error:
        sys.stderr.write(f"Failed to fork: {error}\n")
        sys.exit(1)
