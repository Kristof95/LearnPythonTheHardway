from sys import argv

script, ex15_text = argv

print("We're going to erase %r." % ex15_text)
print("If you don't want that, hit CTRL-C.")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open("C:\\Users\\Kristof\\Desktop\\Learnpythonthehardway\\ex15_text.txt", "w")

print("Truncating the file. Goodbye man!")
target.truncate()


print("Add some data")
line1 = input("Line1:")
line2 = input("Line2:")
line3 = input("Line3:")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it!")
target.close()
