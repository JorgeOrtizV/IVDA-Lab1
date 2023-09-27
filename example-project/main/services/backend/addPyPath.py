import sys
import site
import os

def main(bypass_prompt=False):
	if sys.platform.startswith('win'):        #Then we are in a windows based system.
		pth_dir = os.path.join(sys.prefix, 'Lib', 'site-packages')
	else:
		pth_dir = site.getsitepackages()[0]
		if not os.path.exists(pth_dir):
			os.makedirs(pth_dir)

	# Remove duplicated path files to avoid problems
	for pathfile in ['ivda_app1.pth']:   # Example: [‘ProgramTranslator.pth’]
		pathfile = os.path.join(pth_dir, pathfile)
		if os.path.exists(pathfile):
			print("Removing file: {}".format(pathfile))
			fobj=open(pathfile,"r")
			oldpath=fobj.read()
			fobj.close()
			print("contents: {}".format(oldpath.strip()))
			os.remove(pathfile)
	# Create the new path file
	newpath=os.path.realpath(sys.argv[0]).replace("install.py", "")  # install.py is the name of this script
	pathfile=os.path.join(pth_dir, "ivda_app1.pth") # Ex: ProgramTranslator.pth
	print("Writing file: {}".format(pathfile))
	print(newpath)
	fobj=open(pathfile, "w")
	fobj.write(newpath+"\n")
	fobj.close()

	if not bypass_prompt:
		foo=input("Press ENTER to continue")

if __name__ == "__main__":
	if "--auto" in sys.argv:
		main(True)
	else:
		main(False)
