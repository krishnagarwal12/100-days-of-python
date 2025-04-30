print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
no_of_people = int(input("How many people split the bill? "))
tip_amt = bill*(tip/100)
total_bill = tip_amt + bill
share_of_each_person = round(total_bill/no_of_people,2) #if the result is $33.6, this doesn't return $33.60
share_of_each_person = "{:.2f}".format(share_of_each_person) #this returns $33.60
print(f"Each person should pay ${share_of_each_person}")
