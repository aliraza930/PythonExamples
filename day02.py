print("welcome to the tip calculator!")
bill = float(input("what was the total bill? $"))
tip = int(input("how much tip would you like to give? 10, 12, or 15?"))
people = int(input("how many peoplr to split the bill?"))
bill_with_tip = tip / 100 * bill + bill
print(bill_with_tip)
tip_as_percentage = tip/100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person, 2)
print(f"each person should pay: ${final_amount}")