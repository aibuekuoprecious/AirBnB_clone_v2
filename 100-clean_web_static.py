#!/usr/bin/python3
# Fabfile to delete out-of-date archives.
import os
from fabric.api import env, local, run

env.hosts = ["54.160.85.72", "35.175.132.106"]

def delete_local_archives(number_to_keep=1):
    """Delete out-of-date local archives."""
    number_to_keep = int(number_to_keep)
    if number_to_keep <= 0:
        number_to_keep = 1
    
    local_archive_dir = "versions"
    local_archives = sorted(os.listdir(local_archive_dir))
    archives_to_delete = local_archives[:-number_to_keep]
    
    with lcd(local_archive_dir):
        for archive in archives_to_delete:
            local(f"rm {archive}")

def delete_remote_archives(number_to_keep=1):
    """Delete out-of-date remote archives."""
    number_to_keep = int(number_to_keep)
    if number_to_keep <= 0:
        number_to_keep = 1
    
    remote_archive_dir = "/data/web_static/releases"
    
    with cd(remote_archive_dir):
        archives = run("ls -tr").split()
        archives = [a for a in archives if a.startswith("web_static_")]
        archives_to_delete = archives[:-number_to_keep]
        
        for archive in archives_to_delete:
            run(f"rm -rf {archive}")

def do_clean(number=1):
    """Delete out-of-date archives on both local and remote machines."""
    delete_local_archives(number)
    delete_remote_archives(number)

