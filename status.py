import os
import subprocess
from bench.utils import print_output

for app in os.listdir('./apps'):
	if os.path.isdir(os.path.join('./apps', app)):
		if not app.startswith('.'):
			p = subprocess.Popen(['git', 'status', '-bs'],
					cwd=os.path.join('apps', app), stdout=subprocess.PIPE)
			(out, err) = p.communicate()
			print "\033[1m %-45s \033[0m \033[1m \033[94m %15s \033[0m" % (app, out.rstrip().replace("##", ""))


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
