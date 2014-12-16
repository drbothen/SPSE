videoData = tuple(["SPSE Introduction", 25, 100, 3])
print videoData


videoTitle, runningTime, upVotes, downVotes = videoData

print videoTitle
print runningTime
print downVotes


setA = set([1,2,3,3,2])

print setA


setB = set([3,4,5])

print setB


print setA|setB

print setA&setB

print setA-setB

print setB-setA



myBio = {'name' : 'Joshua', 'age' : 27, 'hobby' : 'hacking'}

print myBio

print myBio.has_key('hobby')


print myBio.has_key('hobbies')

print 'name' in myBio

print 'names' in myBio

print myBio.keys()

print myBio.values()

print myBio.items()

print myBio.get('age')

myBio['Location'] = 'Mars'

print myBio

del myBio['Location']

print myBio

myBio.clear()

print myBio

print dir(myBio)

help(myBio.has_key)