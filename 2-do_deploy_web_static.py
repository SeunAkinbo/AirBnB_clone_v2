#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers, using the function do_deploy:
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ["100.25.158.83", "54.82.178.173"]


def do_deploy(archive_path):
    """Deploys an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_extension = file_name.split(".")[0]
        releases_path = "/data/web_static/releases/"
        current_path = "/data/web_static/current"

        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(releases_path, no_extension))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name,
                                               releases_path, no_extension))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(releases_path,
                                                    no_extension))
        run('rm -rf {}{}/web_static'.format(releases_path, no_extension))
        run('rm -rf {}'.format(current_path))
        run('ln -s {}{}/ {}'.format(releases_path, no_extension, current_path))
        return True
    except Exception as e:
        print(e)
        return False
