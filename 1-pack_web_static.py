#!/usr/bin/python3



def do_pack():
    try:
        local("sudo mkdir -p versions/")
        local("sudo tar -czvf \"./version/web_static_ `date +%Y-%m-%d-%h-%M-%S`\
        .tgz\" web_static")
    except:
        return None
