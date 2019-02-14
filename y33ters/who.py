import subprocess

def who(command, flags, params, output):
	print(subprocess.check_output("who"))
	return