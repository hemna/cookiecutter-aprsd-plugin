import subprocess

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import shutil

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("post_gen_project")

ALL_TEMP_FOLDERS = ["licenses"]

def remove_temp_folders(temp_folders):
    for folder in temp_folders:
        logger.info("Remove temporary folder: %s", folder)
        shutil.rmtree(folder)


if __name__ == "__main__":
    remove_temp_folders(ALL_TEMP_FOLDERS)

    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '*'])
    # This first one will fail due to pre-commit hook failing, which
    # will reformat some files to be compliant.
    subprocess.call(['git', 'commit', '-m', 'Initial commit'])
    # non-compliant files have been modified, so just commit -a
    subprocess.call(['git', 'commit', '-a', '-m', 'Initial commit'])
    subprocess.call(['pre-commit'])
    subprocess.call(['pre-commit', 'install'])

    version = "{{cookiecutter.version}}"
    subprocess.call(['git', 'tag', '-a', version, '-m', 'Initial commit'])
