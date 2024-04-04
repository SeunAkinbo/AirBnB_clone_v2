#!/usr/bin/python3
"""Module - 100-clean_web_static.py"""

import os
from fabric.api import *
env.hosts = ["100.25.158.83", "54.82.178.173"]


def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    """
    number = 1 if int(number) == 0 else int(number)

    local_archives = sorted(os.listdir("versions"), reverse=True)
    for archive in local_archives[number:]:
        local(f"rm versions/{archive}")

    with cd("/data/web_static/releases"):
        remote_archives = run("ls -tr").split()
        remote_archives = [a for a in remote_archives if "web_static_" in a]
        for archive in remote_archives[number:]:
            run(f"rm -rf {archive}")
