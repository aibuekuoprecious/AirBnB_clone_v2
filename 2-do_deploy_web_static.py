#!/usr/bin/python3
"""Fabric script that distributes an archive to web servers"""

from fabric.api import *
import os

# Define the list of host IP addresses
env.hosts = ["34.224.63.159", "3.85.177.105"]


def do_deploy(archive_path):
    """Deploy the archive to the web servers"""
    try:
        # Check if the archive file exists
        if os.path.exists(archive_path):
            # Extract the archive filename without extension
            archive_filename = os.path.basename(archive_path)
            archive_name = os.path.splitext(archive_filename)[0]

            # Define target paths on the remote server
            remote_tmp_path = "/tmp/{}".format(archive_filename)
            remote_release_path = "/data/web_static/releases/{}".format(
                archive_name)

            # Upload the archive to the server
            put(archive_path, remote_tmp_path)

            # Create necessary directories on the remote server
            run('mkdir -p {}'.format(remote_release_path))

            # Extract the archive to the release directory
            run('tar -xzf {} -C {}'.format(remote_tmp_path, remote_release_path))

            # Delete the temporary archive file
            run('rm {}'.format(remote_tmp_path))

            # Move the contents of web_static to the release directory
            run('rsync -av --exclude={}/web_static/images --exclude={}/web_static/styles {}/web_static/* {}/'.format(
                remote_release_path, remote_release_path, remote_release_path, remote_release_path))

            # Update the symbolic link to the new release
            run('rm -rf /data/web_static/current')
            run('ln -s {} /data/web_static/current'.format(remote_release_path))

            # Restart the nginx service
            sudo('service nginx restart')

            print("New version deployed successfully.")
            return True
        else:
            print('File does not exist')
            return False
    except Exception as err:
        print('Error:', err)
        return False
