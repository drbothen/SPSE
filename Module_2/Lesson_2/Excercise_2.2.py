# import python modules

import sys as s
import os as o
import platform as p


# pulls varible from CLI
travDir = s.argv[1]


# manual varible settings for testing
#travDir = "C:/" 



# Performs OS detection and sets the dir seperator char depending on OS
if p.system() == "Windows":
    splitvar = "\\"
    print 'OS type detected: %s'%p.system()
elif p.system() == "Linux":
    splitvar = "/"
    print 'OS type detected: %s'%p.system()
else:
    print 'OS type detected: %s'%p.system() + '/n' + 'No defined split varible, defaulting to \\'
    

# Performs Directory Traversal and prints
for (path, dirs, files) in o.walk(travDir):
    depth_from_root = len(path.split(splitvar))
    print "-"*depth_from_root + '[' + path.split(splitvar)[-1] + ']'
    par_len = len("-"*depth_from_root + '[' + path.split(splitvar)[-1] + ']')
    for file in files:
        print "-"*(par_len +1) + " " + file
