import sys

logOS = open(sys.argv[1], "r")

for line in logOS.readlines():
	if line.lower().find('usb') != -1:
		print line.strip()

