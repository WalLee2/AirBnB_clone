#!/usr/bin/python3
# Generating a .tgz archive from another folder using do_pack fucntion


def do_pack():
    try:
        local("sudo mkdir -p versions/")
        local("tar -czf $(date +'%Y-%m-%d-%h-%M-%s').tar.gz \
        ~/AirBnB_clone/web_static")
    except:
        return
