
# defines the function cheese_and_crackers()
# accepts cheese_count and boxes_of_crackers as arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
# assigns 20 to cheese_count, assigns 30 to boxes_of_crackers
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
# defines variables amount_of_cheese and amount_of_crackers
amount_of_cheese = 10
amount_of_crackers = 50
# inserts variables defined above as the value of cheese_and_crackers() arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
# defines arguments in cheese_and_crackers() as math equations
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
# defines cheese_and_crackers arguments as a combination of previously
# -- defined variables and math for each
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
