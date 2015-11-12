from sys import argv

script, ex15_text = argv

txt = open("C:\\Users\\Kristof\\Desktop\\Learnpythonthehardway\\ex15_text.txt")

print("Here's your file %r:" % ex15_text)
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
