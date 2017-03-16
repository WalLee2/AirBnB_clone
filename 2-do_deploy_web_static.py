#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
from fabric.api import run, env, put
import os

env.hosts = ['52.86.29.108', '54.227.34.170']


def do_deploy(archive_path):
    """
    Wrapping up the tarball and sending it over to a server and opening it
    and "untarballing" it
    """
    if not os.path.isfile(archive_path):
        return False
    try:
        target_name = archive_path.strip("versions/")

        put(archive_path, "/tmp/")
        mystr_0 = "sudo mkdir -p /data/web_static/releases/" + target_name + "/"
        run(mystr_0)
        mystr_1 = "sudo tar -xzf /tmp/" + target_name + \
        " -C /data/web_static/releases/" + target_name + "/"
        run(mystr_1)
        mystr_2 = "sudo rm /tmp/" + target_name
        run(mystr_2)
        mystr_3 = "sudo mv /data/web_static/releases/" + target_name + \
        "/web_static/* /data/web_static/releases/" + target_name + "/"
        run(mystr_3)
        mystr_4 = "sudo rm -rf /data/web_static/releases/" + target_name + \
        "/web_static"
        run(mystr_4)
        mystr_5 = "sudo rm -rf /data/web_static/current"
        run(mystr_5)
        mystr_6 = "sudo ln -s /data/web_static/releases/" + target_name + \
        " /data/web_static/current"
        run(mystr_6)
        print("Executing task 'deploy'")
        return True
    except:
        return False
