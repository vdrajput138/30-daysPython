print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You are allowed to enjoy the ride")
else:
    print("Sorry, you are not allowed to enjoy the ride!")


print("Let's find out whether the number mentioned in Odd or Even!")
number = int(input("Please enter a number.: "))
if number %2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")


# multiple ifs
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
        price = 5
    elif age <= 18:
        print("Please pay $7.")
        price = 7
    else:
        print("Please pay $12.")
        price = 12
    want_photo = input("Do you want to take a picture?(Y/N)")
    if want_photo == "Y" or want_photo == "y":
        print(f"You need to pay the total bill, ${price} + $3 = {price +3} for the ride.")
    else:
        print(f"Enjoy the Ride, your bill for the ride is {price}")
else:
    print("Sorry you have to grow taller before you can ride.")
