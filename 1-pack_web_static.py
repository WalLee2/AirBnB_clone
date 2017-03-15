#!/usr/bin/python3
from fabric.api import *


def do_pack():
    try:
        local("sudo mkdir -p versions/")
        local("sudo tar -czvf \"./versions/web_static `date +%Y-%m-%d-%h-%M-%S`\
        .tgz\" web_static")
    except:
        return None
