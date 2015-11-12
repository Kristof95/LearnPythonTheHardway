from sys import argv

script, username = argv
prompt = '> '

print("Hi %s, I'm the %s script." % (username, script))
print("Do you like me %s?" % username)
likes = input(prompt)

print("Where do you live %s?" % username)
lives = input(prompt)

print("""I've got 2 answer from previous question: %r and %r,
      Thank you!""" % (likes, lives))
