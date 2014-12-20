fdesc = open("spse.txt", "a")

for count in range (0,100):
    fdesc.write(str(count) + "\n")


fdesc.close()


fdesc = open("spse.txt", "r")

for line in fdesc.readlines():
    if line.find("99") != -1:
        print line