from bench.utils import exec_cmd
import os

branch = "develop"

apps_dir = os.path.join('.', 'apps')

apps = [name for name in os.listdir(apps_dir)
    if os.path.isdir(os.path.join(apps_dir, name))]

for app in apps:
    if app in ['erpnext', 'frappe']:
	continue
    app_dir = os.path.join(apps_dir, app)
    if os.path.exists(app_dir):
	try:
        	print("Switching for "+app)
        	exec_cmd("git checkout {branch}".format(branch=branch), cwd=app_dir)
        	exec_cmd("git pull upstream {branch}".format(branch=branch), cwd=app_dir)
	except:
		pass
