#########################################################
# Simple script to install every application into the environment
# Useful when you switch branches for applications with different dependencies
#
# Usage : cd <bench-folder> && ./install_apps.py
#
#########################################################

import os
import subprocess

for app in os.listdir('./apps'):
	if os.path.isdir(os.path.join('./apps', app)):
        # Ignore hidden folders
		if not app.startswith('.'):
			p = subprocess.Popen(['./env/bin/pip', 'install', '-e', './apps/' + app], stdout=subprocess.PIPE)
			(out, err) = p.communicate()
			print out
