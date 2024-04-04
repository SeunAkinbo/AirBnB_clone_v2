#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that distributes an
archive to the web servers, using the function deploy:
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists
env.hosts = ["100.25.158.83", "54.82.178.173"]


def do_pack():
    """Generates a .tgz archive from web_static"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"versions/web_static_{date}.tgz"
        local("mkdir -p versions")
        local(f"tar -cvzf {file_name} web_static")
        return file_name
    except Exception as e:
        print(e)
        return None


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        releases_path = "/data/web_static/releases/"
        current_path = "/data/web_static/current"

        put(archive_path, '/tmp/')
        run(f'mkdir -p {releases_path}{no_ext}/')
        run(f'tar -xzf /tmp/{file_name} -C {releases_path}{no_ext}/')
        run(f'rm /tmp/{file_name}')
        run(f'mv {releases_path}{no_ext}/web_static/* {releases_path}\
                 {no_ext}/')
        run(f'rm -rf {releases_path}{no_ext}/web_static')
        run(f'rm -rf {current_path}')
        run(f'ln -s {releases_path}{no_ext}/ {current_path}')
        return True
    except Exception as e:
        print(e)
        return False


def deploy():
    """Creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
