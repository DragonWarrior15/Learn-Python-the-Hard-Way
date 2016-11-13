def cheese_and_crackers(cheese_count, box_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % box_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket!\n"

print "We can give the function numbers."
cheese_and_crackers(20, 30)

print "Or, we can use variables from our own definitions"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside the arguments too!"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two!"
cheese_and_crackers(amount_of_cheese + 10, amount_of_crackers + 20)
