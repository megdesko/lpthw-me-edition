print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

# set up a poem
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\t where there is none.
"""
# print the poem between 2 lines of dashes
print "--------------"
print poem
print "--------------"

# define a variable called five
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

# define a function that returns the number of 
# jelly beans, jars, and crates needed given the starting number
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

#define a starting point	
start_point = 10000
#then assign three variables to returned vals from this function
beans, jars, crates = secret_formula(start_point)

print "With a starting point of : %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# redefine start point and try again
start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)