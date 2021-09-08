import subprocess

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
version = "{{cookiecutter.version}}"
subprocess.call(['git', 'tag', '-a', version, '-m', 'Initial commit'])
