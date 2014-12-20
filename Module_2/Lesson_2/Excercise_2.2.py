import sys as s
import os as o
import platform as p

travDir = s.argv[1]
#travDir = "C:/"


if p.system() == "Windows":
    splitvar = "\\"
    print 'OS type detected: %s'%p.system()
elif p.system() == "Linux":
    splitvar = "/"
    print 'OS type detected: %s'%p.system()
else:
    print 'OS type detected: %s'%p.system() + '/n' + 'No defined split varible, defaulting to \\'

for (path, dirs, files) in o.walk(travDir):
    depth_from_root = len(path.split(splitvar))
    print "-"*depth_from_root + '[' + path.split(splitvar)[-1] + ']'
    par_len = len("-"*depth_from_root + '[' + path.split(splitvar)[-1] + ']')
    for file in files:
        print "-"*(par_len +1) + " " + file
