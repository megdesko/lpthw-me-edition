people = 30
cars = 40
buses = 15

# if there are more cars than people, print this line
if cars > people:
	print "We should take the cars."

# if there are not more cars than people, and there are more people
# than cars print this line
elif cars < people:
	print "We should not take the cars."

# if neither statement is true, print this	
else: 
	print "We can't decide."
	
# if there are more buses than cars, print this line
if buses > cars:
	print "That's too many buses."

# if there are more cars than buses, and Not more buses than cars
# print this	
elif buses < cars:
	print "Maybe we could take the buses."
# if the number of buses and cars is equal, print this	
else:
	print "We still can't decide."

#if there are more people than buses, print this
if people > buses:
	print "Alright, let's just take the buses."
# if there are not enough buses, print this
else:
	print "Fine, let's stay home then."

#if the number of cars is greater than both the number of buses
# and cars, print this	
if cars > people and buses < cars:
	print "There are lots of cars!"