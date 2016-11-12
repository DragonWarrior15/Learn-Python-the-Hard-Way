from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, i'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
All right, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

# $ python ex14.py zed
# Hi zed, I'm the ex14.py script.
# I'd like to ask you a few questions.
# Do you like me zed?
# >  Yes
# Where do you live zed?
# >  San Francisco
# What kind of computer do you have?
# >  Tandy 1000
# 
# Alright, so you said 'Yes' about liking me.
# You live in 'San Francisco'.  Not sure where that is.
# And you have a 'Tandy 1000' computer.  Nice.
