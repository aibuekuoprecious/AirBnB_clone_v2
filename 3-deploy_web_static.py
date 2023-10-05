#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.
import os
from datetime import datetime
from fabric.api import env, local, put, run

env.hosts = ["54.160.85.72", "35.175.132.106"]

def create_timestamped_archive():
    """Create a timestamped tar gzipped archive."""
    timestamp = datetime.utcnow()
    return timestamp.strftime("%Y%m%d%H%M%S")

def create_archive():
    """Create a tar gzipped archive of the web_static directory."""
    archive_name = create_timestamped_archive()
    archive_path = f"versions/web_static_{archive_name}.tgz"
    
    if not os.path.exists("versions"):
        os.makedirs("versions")
    
    result = local(f"tar -czvf {archive_path} web_static")
    
    if result.succeeded:
        return archive_path
    else:
        return None

def deploy_archive(archive_path):
    """Distribute an archive to a web server."""
    if not os.path.isfile(archive_path):
        return False
    
    file_name = os.path.basename(archive_path)
    folder_name = os.path.splitext(file_name)[0]
    
    remote_tmp_path = f"/tmp/{file_name}"
    releases_path = f"/data/web_static/releases/{folder_name}"
    current_path = "/data/web_static/current"
    
    if put(archive_path, remote_tmp_path).failed:
        return False
    
    if run(f"rm -rf {releases_path}").failed:
        return False
    
    if run(f"mkdir -p {releases_path}").failed:
        return False
    
    if run(f"tar -xzf {remote_tmp_path} -C {releases_path}").failed:
        return False
    
    if run(f"rm {remote_tmp_path}").failed:
        return False
    
    if run(f"mv {releases_path}/web_static/* {releases_path}").failed:
        return False
    
    if run(f"rm -rf {releases_path}/web_static").failed:
        return False
    
    if run(f"rm -rf {current_path} && ln -s {releases_path} {current_path}").failed:
        return False
    
    return True

def deploy():
    """Create and distribute an archive to a web server."""
    archive_path = create_archive()
    
    if archive_path is None:
        return False
    
    return deploy_archive(archive_path)

