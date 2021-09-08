import subprocess

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
# This first one will fail due to pre-commit hook failing, which
# will reformat some files to be compliant.
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
# non-compliant files have been modified, so just commit -a
subprocess.call(['git', 'commit', '-a', '-m', 'Initial commit'])

version = "{{cookiecutter.version}}"
subprocess.call(['git', 'tag', '-a', version, '-m', 'Initial commit'])
