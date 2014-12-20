import user_defined_exceptions as s

try:
    raise s.Networkerror("Bad hostname")
except s.Networkerror, e:
    print e.args

try: # code to try
    a = 0/0
except: # runs only when exception happens
    print "Exception Happened"
else: # runs only if exception did not happen
    print "No Exception"
finally: # runs regardless
    print "Cleanup Code"
    
    
    
try:
    a = 0/0
except ZeroDivisionError:
    print "Divid by Zero"
except:
    print "unknown error"
    



try:
    a = 0/0
except Exception as im:
    print im
    
    


#create user defined exception

