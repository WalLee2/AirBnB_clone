#!/usr/bin/python3
"""
Importing the fabric api
"""
from fabric.api import *
import os
from datetime import datetime

env.hosts = ['52.86.29.108', '54.227.34.170']


def do_pack():
    """
    Making a versions directory and making a tarball
    """
    try:
        local("sudo mkdir -p versions/")
        date_time = datetime.now().strftime("%Y%m%d%H%M%S")
        local("sudo tar -czvf \"./versions/web_static_%s.tgz\" web_static"
              % date_time)
        return os.path.abspath("versions/web_static_{}.tgz".format(date_time))
    except:
        return None


def do_deploy(archive_path):
    """
    Wrapping up the tarball and sending it over to a server and opening it
    and "untarballing" it
    """
    if not os.path.isfile(archive_path):
        return False
    try:
        target_name = archive_path.split("/")[-1]
        simp_name = target_name.split(".")[0]
        put(archive_path, "/tmp/")
        mystr_0 = "sudo mkdir -p /data/web_static/releases/" + simp_name
        run(mystr_0)
        mystr_1 = "sudo tar -xzf /tmp/" + target_name + \
                  " -C /data/web_static/releases/" + simp_name + "/"
        run(mystr_1)
        mystr_2 = "sudo rm /tmp/" + target_name
        run(mystr_2)
        mystr_3 = "sudo mv /data/web_static/releases/" + simp_name + \
                  "/web_static/* /data/web_static/releases/" + simp_name + \
                  "/"
        run(mystr_3)
        mystr_4 = "sudo rm -rf /data/web_static/releases/" + simp_name + \
                  "/web_static"
        run(mystr_4)
        mystr_5 = "sudo rm -rf /data/web_static/current"
        run(mystr_5)
        mystr_6 = "sudo ln -s /data/web_static/releases/" + simp_name + \
                  " /data/web_static/current"
        run(mystr_6)
        print("Executing task 'deploy'")
        return True
    except:
        return False


def deploy():
    """
    Function that tarballs and untarballs files from one server to another
    """
    try:
        archive = do_pack()
        print(archive)
        value = do_deploy(archive)
        return value
    except:
        return False
