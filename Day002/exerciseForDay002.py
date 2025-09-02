"""
    1. Write a program that asks for two numbers and prints their sum, difference, product, and quotient.
"""

input1 = int(input("Please enter the first number:"))
input2 = int(input("Please enter the second number:"))
print(f"Addition of the two numbers provided is : {input1 + input2}")
print(f"Multiplication of the two numbers provided is : {input1 * input2}")
print(f"Division of the two numbers provided is : {input1 / input2}")
print(f"Subtraction of the two numbers provided is : {input1 - input2}")


"""
    2. Create a BMI calculator that takes height (in meters) and weight (in kg) and calculates BMI with 2 decimal places.
"""
#Metric Formula - Weight(kg) / height(m)*height(m)
#imperial formula - [Weight(kg) / height^2(m)] * 703
print("We have two options to calculate BMI. \n Which one way would you like to calculate? \n 1. Metric 2. Imperial")
bmi_opt = input("PLease select the option: ")
if bmi_opt == "1":
    weight_ip = float(input("Please enter the weight in Kg: "))
    height_ip = float(input("Please enter the height in meters: "))
    print(f"Using metric way, your BMI is {weight_ip/ (height_ip * height_ip)}")
elif bmi_opt == "2":
    weight_ip = float(input("Please enter the weight in Kg: "))
    height_ip = float(input("PLease enter the height in meters: "))
    print(f"Using imperial way, your BMI is {(weight_ip / (weight_ip* weight_ip))* 703}")
else:
    print("Please mention the option either 1 or 2.")

"""
    3. Build a simple currency converter that converts dollars to euros (use exchange rate 0.85).

"""
dollors = float(input("Please enter the amount to convert in Euros: "))

amount_in_euros = float(dollors * 0.85)

print(f"The amount of dollors converted in euro is : {amount_in_euros}")



"""
    4. Write a program that calculates how much tip each person should pay when splitting a restaurant bill among friends (include tip percentage).
"""

total_bill = int(input("Total bill amount is?"))
total_people= int(input(" bill will split in how many people?"))
tip_percent = int(input(" tip in %"))
total_amt = (total_bill * (tip_percent/ 100))
print(f" each person will pay {total_amt/ total_people}")

"""
    5. Create a compound interest calculator that takes principal amount, interest rate, and years to calculate final amount.
"""
# compound interest formula A = P(1 + r/n)^(nt)
# simple  interest formula SI - (P * R * T)/100 
sel_opt = input("Welcome to the Interest Calculator:\n Which one would you like to calculate? \n 1. Simple interest \t 2. Compound Interest")
if sel_opt == "1":
    principle_amt= int(input("Please enter amount: "))
    rate_of_interest = float(input("Please enter the rate of interest: "))
    period_of_time = int(input("Please enter the number of years"))
    print(f"Simple interest on {principle_amt} amount is {float((principle_amt * rate_of_interest * period_of_time)/100 ,2)}")
    
elif sel_opt == "2":
    principle_amt= int(input("Please enter amount: "))
    rate_of_interest = float(input("Please enter the rate of interest: "))
    period_of_time = int(input("Please enter the number of years (duration)"))
    compound_time = int(input("Compunding will be :\n 1. Annual 2. Quaterly 3. Monthly"))
    if compound_time == 1:
        comp_time = 1
    elif compound_time == 2:
        comp_time = 4
    elif compound_time == 3:
        comp_time = 12
    else:
        print("We are considering it as annual. you need to provide a number.")
        comp_time =1
    power_op = comp_time * period_of_time
    comp1_calc = 1 +  (rate_of_interest/100)/ period_of_time
    print(f"For Compound interest on {principle_amt}, we will have {comp1_calc ** power_op}")

"""
    6. Build a program that converts seconds into hours, minutes, and remaining seconds format (e.g., "3665 seconds = 1 hour, 1 minute, 5 seconds").
"""
print("We will convert the seconds into hours, minutes and seconds format.")

seconds_input = int(input("Please enter the seconds to convert: "))
secs_remained = seconds_input % 60
minutes_from_seconds = int(seconds_input / 60)

mins_remained = minutes_from_seconds % 60
hours_from_mins = int(minutes_from_seconds / 60)

print(f"{seconds_input} seconds are {hours_from_mins} hours, {minutes_from_seconds} minutes and {secs_remained} seconds.")


"""
    7. Write a temperature converter that can convert between Celsius, Fahrenheit, and Kelvin (user chooses conversion type).
"""
"""
Formulas for Celsius, Fahrenheit, and Kelvin

Celcius to Kelvin  K =  C + 273.15
Kelvin to Celcius C = K - 273.15

Fahrenheit to Celcius  C = (F - 32) * 5/9
Celcius to Fahrenheit  F = c(9/5)+32


Fahrenheit to Kelvin K = (F - 32) * 5/9 + 273.15
Kelvin to Fahrenheit F = (K - 273.15) * 9/5 + 32
"""

print("Hi, you can convert between Celcius, Fehrenheit and Kelvin here.")
print("Plase select which operation you wannt to perform?")
selection_opt = input("""
    1. Celcius to Kelvin
    2. Kelvin to Celcius
    3. Fehrenheit to Kelvin
    4. Kelvin to Fehrenheit
    5. Celcius to Fehrenheit
    6. Fehrenheit to Celcius
    Please mention the choice by number: 
""")
if selection_opt == "1":
    cel_input = float(input("Please enter the temprature value in Celcius: "))
    print("Converted value in Kelvin is: "+ str(cel_input + 273.15))

elif selection_opt == "2":
    kel_input = float(input("Please enter the temprature value in Kelvin: "))
    print(f"Converted value in Celcius is: {kel_input - 273.15}")

elif selection_opt== "3":
    fah_input = float(input("Please enter the temprature value in Fehrenheit: "))
    print(f"Converted value in Kelvin is: {(fah_input - 32)* (5/9) + 273.15}")

elif selection_opt == "4":
    kel_input = float(input("Please enter the temprature value in Kelvin: "))
    print(f"Converted value in Fahrenheit is : {(kel_input - 273.15) * (9/5) + 32}")

elif selection_opt == "5":
    cel_input = float(input("Please enter the temprature value in Celcius: "))
    print(f"Converted value in Fehrenheit is : {cel_input * (9/5) + 32}")

elif selection_opt=="6":
    feh_input = float(input("Please enter the temprature value in Fehrenheit: "))
    print(f"Converted value in Celcius is : {(feh_input - 32) * (5/9)}")

"""
    8. Create a "Life in Weeks" calculator that shows how many weeks you've lived and how many you have left (assuming you'll live to 80).
"""

"""
    9. Build a pizza order calculator that takes pizza size, number of pepperoni, and extra cheese to calculate total cost (define your own pricing).
"""
print("Welcome to the pizza store. Please mention the numbers for the choices below.")
p_orders = int(input("How many pizza would you like to order?(Please mention the count)"))
p_size = int(input("Which pizza size would you prefer? \n1. Small 2. Medium 3. Large"))
p_count = int(input("How many pepperoni would you like to add? ( please mention the count in number)"))
e_cheese = int(input("Would you like to have extra cheese? \n1. Yes 2. No"))
pizza_amount = 0

if p_size == 1:
    pizza_amount+= 10
elif p_size == 2:
    pizza_amount+=20
elif p_size == 3:
    pizza_amount+= 30
else:
    print("Invalid choice.")

if p_count> 0:
    pizza_amount = pizza_amount + (p_count * 2)

if e_cheese == 1:
    pizza_amount+=5

if p_orders >0:
    print(f"Your total bill is {pizza_amount * p_orders} only.")

"""
    10. Write a program that calculates your exact age in years, months, days, hours, minutes, and seconds from your birth date.
"""