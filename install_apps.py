import os
import subprocess
from bench.utils import print_output

for app in os.listdir('./apps'):
	if os.path.isdir(os.path.join('./apps', app)):
		if not app.startswith('.'):
			p = subprocess.Popen(['./env/bin/pip', 'install', '-e', './apps/' + app], stdout=subprocess.PIPE)
			(out, err) = p.communicate()
			print out


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
