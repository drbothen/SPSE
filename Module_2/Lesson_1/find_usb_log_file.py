logOS = open("/var/log/messages","r")

for line in logOS.readlines():
    if line.find('usb') != -1:
        print line