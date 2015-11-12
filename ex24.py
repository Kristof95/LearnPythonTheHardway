#http://learnpythonthehardway.org/book/ex24.html

print("Let's practice everything.")
print("You\ 'd need to know \'bout escapes with \\ that do \n newlines and \t tabs.")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print("------------")
print(poem)
print("------------")

five = 10 - 2 + 3 - 6
print("This should be five: %s" % (five))

def secret(started):
    jelly = started * 500
    jars = jelly / 1000
    crates = jars / 100
    return jelly, jars, crates


start = 10000
jelly, jars, crates = secret(start)

print("With a starting point of: %d" % (start))
print("We'd have %d beans, %d jars, and %d crates." % (jelly, jars, crates))


start /= 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crates." % secret(start))
