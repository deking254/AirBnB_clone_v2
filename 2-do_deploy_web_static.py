#!/usr/bin/python3
import os
from fabric.contrib import files
from fabric.api import local, env, run, task, put, cd
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

"""
@task
@needs_host
def do_deploy(archive_path):
    function to deploy a compressed webm
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
"""


@task
def do_deploy(archive_path):
    """Function to transfer `archive_path` to web servers.

    Args:
        archive_path (str): path of the .tgz file to transfer

    Returns: True on success, False otherwise.
    """
    if not os.path.isfile(archive_path):
        return False
    with cd('/tmp'):
        basename = os.path.basename(archive_path)
        root, ext = os.path.splitext(basename)
        outpath = '/data/web_static/releases/{}'.format(root)
        try:
            putpath = put(archive_path)
            if files.exists(outpath):
                run('sudo rm -rdf {}'.format(outpath))
            run('sudo mkdir -p {}'.format(outpath))
            run('sudo tar -xzf {} -C {}'.format(putpath[0], outpath))
            run('sudo rm -f {}'.format(putpath[0]))
            run('sudo mv -u {}/web_static/* {}'.format(outpath, outpath))
            run('sudo rm -rf {}/web_static'.format(outpath))
            run('sudo rm -rf /data/web_static/current')
            run('sudo ln -sf {} /data/web_static/current'.format(outpath))
            print('New version deployed!')
        except:
            return False
        else:
            return True
