bill1 = input("Enter bill amount: $ ")
tip1 = input("Enter percent tip: ")
split1 = input("Split how many ways?: ")
bill = float(bill1)
tip = float(tip1)
split = float(split1)
if tip > 1:
    tip = tip / 100

tip_cost = bill * tip
total = bill + tip_cost
per_person = total / split

print("The total with tip is ${}".format(total))
print("Each person owes ${}".format(per_person))
