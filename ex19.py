#http://learnpythonthehardway.org/book/ex19.html


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Yaman Rasstafari")
    print("My money is long")

print("give the func number directly:")
cheese_and_crackers(20,30)

print("OR, we can use variable from our script:")
amountofcheese=10
amountofcrackers=50

cheese_and_crackers(amountofcheese, amountofcrackers)

print("We can even do math inside too:")

cheese_and_crackers(10 + 20, 5 + 3)

print("And we can combine the two, variable and math:")
cheese_and_crackers(amountofcheese + 20, amountofcrackers + 300)
    
