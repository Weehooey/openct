"""Daemon Module.
"""

import os
import signal
import daemon

from openct.setup import Config


def sigterm_handler(signum, frame) -> None:
    """Terminate the daemon."""
    raise SystemExit(0)


def daemonize(config: Config) -> None:
    # Create the daemon context
    context = daemon.DaemonContext(
        working_directory=config.dirs.root_dir,
        umask=0o002,
        pidfile=daemon.pidfile.PIDLockFile("/var/run/openct.pid"),
    )

    # Signal handlers
    context.signal_map = {
        signal.SIGTERM: sigterm_handler,
        signal.SIGHUP: "sigterm_handler",
    }

    # Open files to preserve
    context.files_preserve = []

    # Run the daemon
    with context:
        pass
