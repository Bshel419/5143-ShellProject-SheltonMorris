import subprocess

def who():
	print(subprocess.check_output("who"))
	return