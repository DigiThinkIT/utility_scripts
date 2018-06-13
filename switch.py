#########################################################
# Simple script to change the branch for each application in the apps folder
# Useful when you want to change to a different branch for each application
# Assumes that you DON'T have the branch on your local 
#
# Usage : cd <bench-folder> && python quick_switch.py [branch]
#
#########################################################


from bench.utils import exec_cmd
import os
import sys


if len(sys.argv) != 2:
    print "Usage: python switch.py [branch]"
    sys.exit(1)

branch = sys.argv[1]
apps_dir = os.path.join('.', 'apps')

apps = [name for name in os.listdir(apps_dir)
    if os.path.isdir(os.path.join(apps_dir, name))]

for app in apps:
    app_dir = os.path.join(apps_dir, app)
    if os.path.exists(app_dir):
	try:
        	print("Switching for "+app)
        	unshallow = "--unshallow" if os.path.exists(os.path.join(app_dir, ".git", "shallow")) else ""
        	exec_cmd("git config --unset-all remote.upstream.fetch", cwd=app_dir)
        	exec_cmd("git config --add remote.upstream.fetch '+refs/heads/*:refs/remotes/upstream/*'", cwd=app_dir)
        	exec_cmd("git fetch upstream {unshallow}".format(unshallow=unshallow), cwd=app_dir)
        	exec_cmd("git checkout {branch}".format(branch=branch), cwd=app_dir)
        	exec_cmd("git pull upstream {branch}".format(branch=branch), cwd=app_dir)
	except:
		pass
