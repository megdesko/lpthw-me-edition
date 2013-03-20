# create a string named ten_things
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait, there's not 10 things in that list, let's fix that."

# break apart ten_things on ' ' into a list
stuff = ten_things.split(' ')
# make a list of strings called more_stuff
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# while there are fewer than 10 items in the stuff list, add more from more_stuff
# using by "popping" off the "end" of the list
while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)

# print the resulting stuff	
print "There we go: ", stuff

print "Let's do some things with stuff."

# print the second item in the stuff list
print stuff[1]
# print the last item in the stuff list
print stuff[-1] # whoa! fancy
#print the last item in the stuff list
print stuff.pop()
# print the result of combining all elements in stuff with ' ' between them
print ' '.join(stuff) #what?  cool!
# print elements from the 4th to < the 6th with a # between them
print '#'.join(stuff[3:5]) # super stellar!