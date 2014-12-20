import os
import glob

print os.getcwd()


os.mkdir("Test Dir")

os.listdir(".")


for items in os.listdir("."):
    if os.path.isfile(items):
        print items + " is a file"
    elif os.path.isdir(items):
        print items + " is a directory"
    else:
        print "unknown"



for item in glob.glob(os.path.join(".", "*.txt")):
    print item