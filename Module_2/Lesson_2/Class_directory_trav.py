import os
import glob

print os.getcwd()


#os.mkdir("Test Dir")

os.listdir(".")


for items in os.listdir("."):
    if os.path.isfile(items):
        print items + " is a file"
    elif os.path.isdir(items):
        print items + " is a directory"
    else:
        print "unknown"



for item in glob.glob(os.path.join(".", "*.py")):
    print item.split("\\")[-1]
    
    
    
print "here is glob: ", os.path.join(".", "*.py")




#infoStat = os.stat('C:/Sandbox\\jmagady\\Programmig\\drive\\C\\Documents and Settings\\jmagady\\Documents\\GitHub\\Coursera\\An-Introduction-to-Interactive-Programming-in-Python\\Week_3\\String_proc.py')

#print str(infoStat.st_size)