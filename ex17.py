#using some libraries
from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print the file names
print "Copying from %s to %s" % (from_file, to_file)

# read the data from one file and set var
indata = open(from_file).read()

#finding the length of the incoming file
print "The input file is %d bytes long" % len(indata)

#check to see if output file exists
print "Does the output file exist? %r" % exists(to_file)
#confirm that we want to replace the file if exists
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

#write the file out
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

#close output file files
out_file.close()
