from decimal import Rounded


print("Welcome to the tip calculator.")

bill = float(input("What was the total bill?\n"))
perc = float(input("What percentage would you like to give?\n"))
split = int(input("How many people split the bill?\n"))

calculation = round(float(bill) / int(split),2) * float(perc)

bill_per_person = bill /split

final_amount = round(bill_per_person,2)
final_amount = "{:2f}".format(bill_per_person)


print(f"Each person should pay ${final_amount}" )



