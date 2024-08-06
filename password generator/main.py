import string,os,sys
#from subprocess import getoutput
from random import choice

class main:
	def __init__(self):
		self.main()
	def banner(self):
		os.system("cls" if os.name=="nt" else "clear")
		print("""\33[1;31m
          ▄▀▄     ▄▀▄
         ▄█░░▀▀▀▀▀░░█▄
     ▄▄  █░░░░░░░░░░░█  ▄▄
    █▄▄█ █░░█░░┬░░█░░█ █▄▄█{1}
╔════════════════════════════════════════╗
║{0} ♚ Project {1}:{0} ℙ𝕒𝕤𝕤𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣™             {1}║
║{0} ♚ Author  {1}:{0} Lusmaysh                   {1}║
║{0} ♚ Github  {1}:{0} github.com/Lusmaysh        {1}║
║{0} ♚ Version {1}:{0} v1.0.0                     {1}║
╚════════════════════════════════════════╝\33[0m""".format("\33[32;1m","\33[36;1m"))
	def main(self):
		self.banner()
		char=input("{0}[{3}+{0}] {1}Number of characters: {2}".format("\33[1;34m","\33[33;1m","\33[1;36m","\33[1;35m"))
		if not char or not char.isdigit():
			char=8
		line=input("{0}[{3}+{0}] {1}Number of lines: {2}".format("\33[1;34m","\33[33;1m","\33[1;36m","\33[1;35m"))
		if not line or not line.isdigit():
			line=10
		print("═"*42)
		for x in range(int(line)):
			result="".join(choice(string.ascii_letters + string.digits + "-_.{}*&^%$#@!") for c in range(int(char)))
			print(f"\33[1;34m[\33[1;35m{x+1}\33[1;34m] \33[1;36m{result}\33[0m")

if __name__=="__main__":
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()