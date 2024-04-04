#!/usr/bin/python3
"""Module - 3-deploy_web_static"""

from fabric.api import put, run, env, local
from datetime import datetime
env.hosts = ["100.25.158.83", "54.82.178.173"]


def do_pack():
    """The script generates a .tgz archive from web_static"""

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive = "versions/web_static_{}.tgz".format(time)

    local("mkdir -p versions")
    convert = local("tar -cvzf {} web_static".format(archive))

    if convert.failed:
        return None
    return archive


def do_deploy(archive_path):
    """Deploys an archive to the web servers"""
    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_extension = file_name.split(".")[0]
        releases_path = "/data/web_static/releases/"
        current_path = "/data/web_static/current"

        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(releases_path, no_extension))
        run("tar -xzf /tmp/{} -C {}{}/".format(file_name,
                                               releases_path, no_extension))
        run("rm /tmp/{}".format(file_name))
        run("mv {0}{1}/web_static/* {0}{1}/".format(releases_path,
                                                    no_extension))
        run("rm -rf {}{}/web_static".format(releases_path, no_extension))
        run("rm -rf {}".format(current_path))
        run("ln -s {}{}/ {}".format(releases_path, no_extension, current_path))
        return True
    except Exception as e:
        print(e)
        return False


def deploy():
    """Deploys archive to the web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
