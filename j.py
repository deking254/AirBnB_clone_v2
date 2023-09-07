#!/usr/bin/python3
from fabric.api import local, env, run, task
env.hosts = ["were","ert"]
print(env)
