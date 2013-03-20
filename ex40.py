# create a dict with key value pairs of state: city
cities = {'CA': 'San Francisco', 'MI': 'Detroit', 
					'FL': 'Jacksonville'}

# add a couple more by indexing them directly					
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# function that returns the city if the state is present
def find_city(themap, state):
	if state in themap:
		return themap[state]
	else:
		return "Not found."
		
# ok pay attention!
# put the find_city function into cities dict, keyed off of _find
cities['_find'] = find_city
# as long as there are the correct # of inputs, keep running this loop
while True:
	print "State? (ENTER to quit)",
	# get the state inputted from the command line
	state =  raw_input("> ")
	
	# if there is no state entered, quit the program
	if not state: break
	
	#this line is the most important ever!  study!
	# set city_found = calling find_city on cities dict, incoming state
	city_found = cities['_find'] (cities, state)
	print city_found
	