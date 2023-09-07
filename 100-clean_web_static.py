#!/usr/bin/python3
import os
from fabric.api import local, env, run, task, put, lcd, cd
from fabric.network import needs_host
import datetime
name = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
final_name = 'web_static_' + name + ".tgz"
d = final_name.partition('.')[0]
env.hosts = ['100.27.10.6', '54.236.25.48']
env.user = 'ubuntu'


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
    fl = archive_path.partition("/")[2]
    f = fl.partition('.')[0]
    r = "/data/web_static/releases/"
    if os.path.exists(archive_path):
        try:
            put(archive_path,  "/tmp/")
            run("sudo mkdir -p /data/web_static/releases/" + f)
            run("sudo tar -xzf /tmp/" + fl + " -C " + r + f)
            run("sudo rm /tmp/" + fl)
            run("sudo rm -r " + r + f + "/images")
            run("sudo rm -r " + r + f + "/styles")
            run("sudo mv -f " + r + f + "/web_static/* " + r + f)
            run("sudo rm -rf " + r + f + "/web_static")
            run("sudo rm -rf /data/web_static/current")
            run("sudo ln -s " + r + f + " " + "/data/web_static/current")
            return (True)
        except Exception as e:
            print("error")
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

@task
def do_clean(number=0):
        """deletes out-of-date archives, using the function"""
        loc = 'ls -t /data/web_static/releases/ | grep .tgz'
        r = "/data/web_static/releases/"
        t = 'test -d {}'
        with lcd('versions'):
            try:
                archives = local('ls -t', capture=True).split('\n')
                print(archives)
                if number == 0 or int(number) == 0:
                    number = 1
                if len(archives) >= int(number):
                    new = archives[int(number):]
                    if len(new) > 0:
                        for n in new:
                            local('rm ' + n)
                        print("removed all local files")
                        archives = run(loc, capture=True).split('\n')
                        if number == 0 or int(number) == 0:
                            number = 1
                        if len(archives) >= int(number):
                            new = archives[int(number):]
                            for n in new:
                                folder = r + n.split('.')[0]
                                if run(t.format(folder)).succeeded:
                                    run('rm -rf {}'.format(folder))
                            run('ls -l /data/web_static/releases/')
            except Exception as e:
                print(e)
