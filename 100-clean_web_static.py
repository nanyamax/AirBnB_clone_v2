#!/usr/bin/env python3
"""
Fabric script to delete out-of-date archives
"""

from fabric.api import *
from os import path

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'
env.key_filename = '/path/to/ssh/key'

def do_clean(number=0):
    """
    Deletes all unnecessary archives in the versions folder
    Deletes all unnecessary archives in the /data/web_static/releases folder
    """
    number = int(number)
    if number < 1:
        number = 1
    with lcd('./versions'):
        local('ls -t | tail -n +{} | xargs rm -rf --'.format(number + 1))
    with cd('/data/web_static/releases'):
        run('ls -t | tail -n +{} | xargs rm -rf --'.format(number + 1))
