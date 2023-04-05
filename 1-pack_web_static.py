#!/usr/bin/python3
"""
This module contains the function do_pack, which generates a .tgz archive from
the contents of the web_static folder (fabric script)
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Create a compressed archive of the web_static directory"""

    # Create the 'versions' directory if it doesn't already exist
    local("mkdir -p versions")

    # Get the current timestamp to use as the archive filename
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(timestamp)

    # Create a compressed archive of the web_static directory
    command = "tar -cvzf {} web_static".format(archive_name)
    result = local(command)

    # Return the archive path if successful, None otherwise
    if result.failed:
        return None
    else:
        return archive_name
