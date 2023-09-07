#!/usr/bin/python3
import os
from fabric.api import local, env, run, task, put
from fabric.network import needs_host
import datetime
name = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
final_name = 'web_static_' + name + ".tgz"
d = final_name.partition('.')[0]
env.hosts = ['100.27.10.6', '54.236.25.48']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


@task
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


@task
@needs_host
def do_deploy(archive_path):
    """function to deploy a compressed web"""
    fl = archive_path.partition("/")[-1]
    f = fl.partition('.')[0]
    r = "/data/web_static/releases/"
    if os.path.exists(archive_path):
        try:
            put(archive_path,  "/tmp/")
            run("sudo mkdir -p /data/web_static/releases/" + f)
            run("sudo tar -xzf /tmp/" + fl + " -C " + r + f)
            run("sudo rm /tmp/" + fl)
            run("sudo mv -u " + r + f + "/web_static/* " + r + f)
            run("sudo rm -rf " + r + f + "/web_static")
            run("sudo rm -rf /data/web_static/current")
            run("sudo ln -s " + r + f + " " + "/data/web_static/current")
            return (True)
        except Exception as e:
            print("error")
            return (False)
    else:
        return (False)
