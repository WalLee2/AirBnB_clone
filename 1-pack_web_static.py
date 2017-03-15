#!/usr/bin/python3
"""
Importing the fabric api
"""
from fabric.api import *


def do_pack():
    """
    Making a versions directory and making a tarball
    """
    try:
        local("sudo mkdir -p versions/")
        local("sudo tar -czvf \"./versions/web_static `date +%Y-%m-%d-%h-%M-%S`\
        .tgz\" web_static")
    except:
        return None
