byte = input("\n> ")

if len(byte) > 0:
    print("Byte: " + byte)

    bit = 8
    byte_as_int = int(byte)
    choose = input("\nDo you want to change byte to bit?(y / n) > ")

    if choose.lower() == "y":
        print("Byte: " + byte)
        print()
        print("Bit: %d" % (bit*byte_as_int))
    elif choose.lower() == "n":
        print("Goodbye! Have a nice day!")
        quit()

