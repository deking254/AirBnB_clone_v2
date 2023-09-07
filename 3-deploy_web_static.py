#!/usr/bin/python3
import os
from fabric.api import local, env, run, task, put
from fabric.network import needs_host
import datetime
name = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
final_name = 'web_static_' + name + ".tgz"
directory = final_name.partition('.')[0]
env.hosts = ['ubuntu@100.27.10.6', 'ubuntu@54.236.25.48']


@task
def do_pack():
    """script that generates a .tgz archive"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/" + final_name + " ./web_static")
    except Exception as e:
        return (None)
    if os.path.exists("versions/" + final_name):
        return ("versions/" + final_name)
    else:
        return (None)


@task
@needs_host
def do_deploy(archive_path):
    """function to deploy a compressed web"""
    fl = archive_path.partition("/")[2]
    f = fl.partition('.')[0]
    r = "/data/web_static/releases/"
    if os.path.exists(archive_path):
        try:
            put(archive_path,  "/tmp/")
            run("sudo mkdir -p /data/web_static/releases/" + f)
            run("sudo tar -xzf /tmp/" + fl + " -C " + r + f)
            run("sudo rm /tmp/" + fl)
            run("sudo mv -r " + r + f + "/web_static/* " + r + f)
            run("sudo rm -rf " + r + f + "/web_static")
            run("sudo rm -rf /data/web_static/current")
            run("sudo ln -s " + r + f + " " + "/data/web_static/current")
            return (True)
        except Exception as e:
            return (False)
    else:
        return (False)


@task
def deploy():
    """the function to deploy the website"""
    try:
        path = do_pack()
        deploy = do_deploy(path)
        return (deploy)
    except Exception as e:
        return (False)
