# this one is like argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1 : %r, arg2 : %r" % (arg1, arg2)

# can be done this way too
def print_two_again(arg1, arg2):
	print "arg1 : %r, arg2 : %r" % (arg1, arg2)

# takes just one argument
def print_one(arg1):
	print "arg1 : %r" % arg1

# no argument
def print_none():
	print "I got nothing."

print_two('Zed', 'Shaw')
print_two_again('Zed', 'Shaw')
print_one('Zed')
print_none
