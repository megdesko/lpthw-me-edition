#importing a library(?)
from sys import argv

script, filename = argv
# decide whether to erase the file name
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
#get the response
raw_input("?")


# say you're going to open file, open in write mode
print "Opening the file..."
target = open(filename, 'w')
#truncate the file
print "Truncating the file.  Goodbye!"
target.truncate()

#get info to put in the file
print "Now I'm going to ask you for three lines."

#store information in variables
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

#print out what is going to happen next: adding to file
print "I'm going to write these to the file."

# add the input of line 1 to file, with newline
target.write(line1)
target.write("\n")
# add the input of line 2 to file, add newline
target.write(line2)
target.write("\n")
#add the input of line 3 to file, add newline
target.write(line3)
target.write("\n")

print "And finally, we close it."
#close the file
target.close()
# the file is closed.  Yippee!