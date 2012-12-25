

def add_and_print_numbers(my_number):
	i = 0
	numbers = []
	while i < my_number:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i += 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	print "The numbers: "
	for num in numbers:
		print num	
	

numbers = [] # initialize an empty list
my_number = 17
add_and_print_numbers(my_number)


## rewrite with for loop
def add_and_print_numbers2(my_number):
	i = 0
	numbers = []
	for i in range(i, my_number):
		print "At the top i is %d" % i
		numbers.append(i)
	
		i += 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	print "The numbers: "
	for num in numbers:
		print num	
	

numbers = [] # initialize an empty list
my_number2 = 17
add_and_print_numbers2(my_number2)

