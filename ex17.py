from sys import argv
from os.path import exists

script, ex15_text, ex17_tofile = argv

print("Copying from %s to %s" % (ex15_text, ex17_tofile))

in_file = open("C:\\Users\\Kristof\\Desktop\\Learnpythonthehardway\\ex15_text.txt")
indata = in_file.read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(ex17_tofile))
print("Ready, hit the RETURN to continue, CTRL-C to abort.")
input()

out_file = open("C:\\Users\\Kristof\\Desktop\\Learnpythonthehardway\\ex17_tofile.txt", "w")
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
