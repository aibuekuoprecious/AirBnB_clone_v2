#!/usr/bin/python3
# Fabfile to generate a .tgz archive from the contents of web_static.
import os
from fabric.api import local
from datetime import datetime

def create_timestamped_archive():
    """Create a timestamped tar gzipped archive."""
    timestamp = datetime.utcnow()
    return timestamp.strftime("%Y%m%d%H%M%S")

def create_archive():
    """Create a tar gzipped archive of the directory web_static."""
    archive_name = create_timestamped_archive()
    archive_path = f"versions/web_static_{archive_name}.tgz"
    
    if not os.path.exists("versions"):
        os.makedirs("versions")
    
    result = local(f"tar -czvf {archive_path} web_static")
    
    if result.succeeded:
        return archive_path
    else:
        return None

def do_pack():
    """Pack the web_static directory and return the archive path."""
    archive_path = create_archive()
    return archive_path

