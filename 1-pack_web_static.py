#!/usr/bin/python3
"""Module - 1-pack_web_static.py"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """The script generates a .tgz archive from web_static"""

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive = "versions/web_static_{}.tgz".format(time)

    local("mkdir -p versions")
    convert = local("tar -cvzf {} web_static".format(archive))

    if convert.failed:
        return None
    return archive
