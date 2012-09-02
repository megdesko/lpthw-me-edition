#using some libraries
from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print the file names
print "Do you want to copy from %s to %s?" % (from_file, to_file)

print "RETURN to continue, CTRL-C to abort."
raw_input()

# read the data from one file and write it
open(to_file, 'w').write(open(from_file).read())
