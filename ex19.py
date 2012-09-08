# define a function that will print out
# information about how much cheese and crackers there are

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
# add numbers as the arguments to the function and execute it.
print "We can just give the funciton numbers directly:"
cheese_and_crackers(20, 30)

#create variables with stored values
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# Then use those variables as arguments to a function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# arithmetic expressions can be function arguments as well
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# pass in arithmetic done with variables as arguments to function
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)