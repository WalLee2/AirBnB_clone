#!/usr/bin/python3
"""
Importing the fabric api
"""
from fabric.api import *
import os
from datetime import datetime

def do_pack():
    """
    Making a versions directory and making a tarball
    """
    try:
        local("sudo mkdir -p versions/")
        date_time = datetime.now().strftime("%Y%m%d%h%M%S")
        local("sudo tar -czvf \"./versions/web_static_%s.tgz\" web_static" % date_time)
        return os.path.abspath("versions/")
    except:
        return None
