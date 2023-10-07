#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os
from fabric.api import env, put, run

env.hosts = ["34.224.63.159", "3.85.177.105"]
env.user = "ubuntu"  # Set the SSH username
env.key_filename = "~/.ssh/school"  # Set the path to your SSH private key


def file_exists(path):
    """Check if a file exists on the remote server."""
    return run(f"test -e {path}", warn_only=True).succeeded


def deploy_archive(archive_path):
    """Distribute an archive to a web server."""
    if not os.path.isfile(archive_path):
        return False

    # Add debug statements to check each step
    print(f"Uploading archive: {archive_path}")
    if put(archive_path, remote_tmp_path).failed:
        print("Failed to upload archive")
        return False
    print("Archive uploaded successfully")

    # Extract archive name and folder name
    file_name = os.path.basename(archive_path)
    folder_name = os.path.splitext(file_name)[0]

    # Define paths
    remote_tmp_path = f"/tmp/{file_name}"
    releases_path = f"/data/web_static/releases/{folder_name}"
    current_path = "/data/web_static/current"

    # Upload the archive to the remote server
    if put(archive_path, remote_tmp_path).failed:
        return False

    # Create a new release directory
    if run(f"mkdir -p {releases_path}").failed:
        return False

    # Extract the archive into the new release directory
    if run(f"tar -xzf {remote_tmp_path} -C {releases_path}").failed:
        return False

    # Remove the uploaded archive from /tmp
    if run(f"rm {remote_tmp_path}").failed:
        return False

    # Move the contents of the release directory to current
    if run(f"mv {releases_path}/web_static/* {releases_path}").failed:
        return False

    # Remove the now empty web_static folder
    if run(f"rm -rf {releases_path}/web_static").failed:
        return False

    # Update the symbolic link
    if run(f"rm -rf {current_path} && ln -s {releases_path} {current_path}").failed:
        return False

    return True


def do_deploy(archive_path):
    """Distribute an archive to a web server and return success status."""
    return deploy_archive(archive_path)
