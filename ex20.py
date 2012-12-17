# use argv for working with this file
from sys import argv

# set the values of inputs from the command line
script, input_file = argv

# define a function to print everything in the file
def print_all(f):
	print f.read()
	
# define a function that finds the 0th line in the file
def rewind(f):
	f.seek(0)
	
# define a function that will print a particular line
def print_a_line(line_count, f):
	print line_count, f.readline()
	
# the file we are looking at is the file that was
# the input, after being opened
current_file = open(input_file)

print "First let's print the whole file:\n"

# write out the contents of the whole file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# go back to the first position in the file
rewind(current_file)

print "Let's print three lines:"

# set the current line = line 1
current_line = 1
# then print a line
print_a_line(current_line, current_file)

# add 1 to the current line (now it's 2)
current_line += 1
# and print line 2
print_a_line(current_line, current_file)

# add 1 to the current line, so now it's 3
current_line += 1
# and then print line 3
print_a_line(current_line, current_file)