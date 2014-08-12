#! /usr/bin/python
#encoding=utf-8

__author__ = "fakir"

from fabric.api import *
from fabric.colors import *

import time

env.use_ssh_config=True
env.hosts = ["server"]

def setup_dirs():
    with cd("/home/ubuntu"):
        if run("test -d backup").succeeded:
            run("rm -rf backup/*")
        else:
            run("mkdir backup")

def backup_database():
    with cd("/home/ubuntu/backup"):
        run("mysqldump -uroot -p wordpress | gzip > wordpress.sql.gz")

def compress_backup():
    with cd("/home/ubuntu"):
        with settings(warn_only=True):
            run("tar -zc -f smalllv.tar.gz backup")

def wordpress():
    execute("setup_dirs")
    with cd("/home/ubuntu"):
        run("cp -r wordpress backup")

    execute("backup_database")
    execute("compress_backup")
    with cd("/home/ubuntu"):
        get("smalllv.tar.gz", "/home/shao/work/Cloud/smalllv/%s-all.tar.gz" % time.strftime("%Y%m%d"))
        run("rm -rf smalllv.tar.gz")


def wordpressdb():
    execute("setup_dirs")
    execute("backup_database")
    execute("compress_backup")
    with cd("/home/ubuntu"):
        get("smalllv.tar.gz", "/home/shao/work/Cloud/smalllv/%s-db.tar.gz" % time.strftime("%Y%m%d"))
        run("rm -rf smalllv.tar.gz")
