bit = input("8 bit: ")
result = 0

lst = [1,2,4,8,16,32,64,128]
for i in bit:
    if i == "1":
        for x in lst:
            result += x

print(bit + " to " + "%d" % result)

