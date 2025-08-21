print("Welcome to the Tip Calculator! \n")
total_bill = float(input("What was the total bill? "))
tip = float(input("how much tip would you like to give? (In percent) 10,20,25: "))
people = int(input("Bill is split between how many people? "))
if people > 0 and total_bill > 0 and tip > 0:
    tip_amount = total_bill * (tip/100)
    final_amount = tip_amount + total_bill
    per_person = round((final_amount / people),2)
    print("Each person will pay : $" + str(per_person) + " the bill")
else:
    print("Please provide the valid amount for people, total bill and tip percentage")

