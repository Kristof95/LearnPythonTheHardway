def story():
    print("Welcome AHYA!")
    print("""Your name is AHYA
You're a warrior, in a merciless world
your purpose is protect your village
from the trolls, if you want to 
make an end of trolls attack,
you must kill them.""")

def fight():
    begin = input("Do you want to kill some trolls?:")
    if begin.lower() == "y":
        attack_form()
    elif begin.lower() == "n":
        print("A real fighter never give up!")
        noob()
    else:
        quit()

def attack_form():
    attack = input("Which fight form will you choose assa or curse?")
    if attack == "assa":
        print("The trolls dead.")
        congratulation()
    elif attack == "curse":
        print("The curse is add more strength to the trolls, you died.")
        noob()
    else:
        quit()

def congratulation():
    print("You completed your purpose Congrat!! You're a real fighter!")


def noob():
    print("do harakiri yourself you're not a real fighter you're a bunny!")

story()
fight()
