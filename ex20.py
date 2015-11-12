#http://learnpythonthehardway.org/book/ex20.html

from sys import argv

script, input_file = argv

def print_all(f):
    print (f.read())

def rewind(f):
    f.seek(0)

def printaline(linec, f):
    print(linec, f.readline())

currentfile = open("C:\\Users\\Kristof\\Desktop\\Learnpythonthehardway\\simple.txt", "r")

print("First let's print the whole file :\n")

print_all(currentfile)

print("Now let's rewind, kind of like a tape.")

rewind(currentfile)

print("Let's print three lines:")

currentline = 1
printaline(currentline, currentfile)

currentline += 1
printaline(currentline, currentfile)

