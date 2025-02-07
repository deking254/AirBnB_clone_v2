#!/usr/bin/python3
import os
from fabric.api import local
import datetime
name = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
final_name = 'web_static_' + name + ".tgz"


def do_pack():
    """script that generates a .tgz archive"""
    if os.path.exists("versions/" + final_name):
        return ("versions/" + final_name)
    else:
        try:
            local("mkdir -p versions")
            local("tar -cvzf versions/" + final_name + " ./web_static")
            return ("versions/" + final_name)
        except Exception as e:
            return (None)
