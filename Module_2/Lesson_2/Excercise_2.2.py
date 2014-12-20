'''
This is a directory traversal tool. first arg is for the starting directory and the optional 2nd arg is for the file(s) or type(s) your looking for.
on linux systems you may have to use quotes around your 2nd arg
'''





# import python modules

import sys as s
import os as o
import platform as p
import glob
import datetime

# pulls varible from CLI

travDir = s.argv[1]

try:
    fileType = s.argv[2]

except:
    fileType = ""
    
try:
    fileDetails = s.argv[3]
    
except:
    fileDetails = ""

# manual varible settings for testing
#travDir = "C:/" 
#fileType = "*.txt"
#fileDetails = "-d"

# Performs OS detection and sets the dir seperator char depending on OS
if p.system() == "Windows":
    splitvar = "\\"
    print 'OS type detected: %s'%p.system()
elif p.system() == "Linux":
    splitvar = "/"
    print 'OS type detected: %s'%p.system()
else:
    print 'OS type detected: %s'%p.system()
    print 'No defined split varible, defaulting to \\'
    splitvar = "\\"
    
fileCount = 0
# Performs Directory Traversal and prints
for (path, dirs, files) in o.walk(travDir):
    if fileType != "":
        
        if glob.glob(o.path.join(path, fileType)) != []:
            depth_from_root = len(path.split(splitvar)) # calculates how far from the starting directory you are
            print "-"*depth_from_root + '[' + path.split(splitvar)[-1] + ']' # prints foler names
            par_len = len("-"*depth_from_root + '[' + path.split(splitvar)[-1] + ']') # Calculates distance for files
            for file in glob.glob(o.path.join(path, fileType)):
                fileCount += 1
                if fileDetails != "":
                    infoStat = o.stat(o.path.join(path,file.split(splitvar)[-1]))
                    print "-"*(par_len +1) + " " + file.split(splitvar)[-1] + " "*(4) + 'Size: ' + str(infoStat.st_size) + " "*(4) + 'Last Access: ' + str(datetime.datetime.fromtimestamp(infoStat.st_atime).strftime('%Y-%m-%d %H:%M:%S'))
                else:
                    print "-"*(par_len +1) + " " + file.split(splitvar)[-1]
    else:
        depth_from_root = len(path.split(splitvar))
        print "-"*depth_from_root + '[' + path.split(splitvar)[-1] + ']'
        par_len = len("-"*depth_from_root + '[' + path.split(splitvar)[-1] + ']')
        for file in files:
            fileCount += 1
            print "-"*(par_len +1) + " " + file
            
print "Directory Traversal Completed"
print "%d files where found"%fileCount  


#o.path.join(path)