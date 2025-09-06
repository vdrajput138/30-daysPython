"""






5. Password Strength Checker

Requirements: 8+ chars, 1 uppercase, 1 lowercase, 1 number, 1 special char
Output: Weak/Medium/Strong with specific feedback
Handle: Empty strings, spaces only"""



"""
    1. Grade Calculator (Enhanced)

Input: Multiple subject marks (at least 5 subjects)
Calculate average, assign letter grade, determine if student passes (>60%)
Handle invalid marks, divide by zero

"""

print("Welcome to the Grade calcultion program!")
print("We will be calculating the grade based on following subjects: \n 1. English 2. Secondary Language 3. Maths 4. Social Science 5. Environmental Science 6. Physical Test")

student_name = input("Please mention student name: ")
eng_sub = int(input(f"Please enter the marks obtained for English subject by {student_name}: "))
sed_sub = int(input(f"Please enter the marks obtained for secondary language by {student_name}: "))
maths_sub = int(input(f"Please enter the marks obtained for Maths by {student_name}: "))
social_science = int(input(f"Please enter the marks obtained for Social Science by {student_name}: "))
env_sci = int(input(f"Please enter the marks obtained for Environmental Science by {student_name}: "))
phy_test = int(input(f"Please enter the marks obtained for Physical Tests by {student_name}: "))

if eng_sub < 0 or eng_sub > 100:
    eng_sub = 0
if sed_sub < 0 or sed_sub > 100:
    sed_sub = 0
if maths_sub < 0 or maths_sub > 100:
    maths_sub = 0
if social_science < 0 or social_science > 100:
    social_science = 0
if env_sci < 0 or env_sci >  100:
    env_sci = 0
if phy_test < 0 or phy_test > 100:
    phy_test = 0

average_score = (eng_sub + sed_sub + maths_sub + social_science + env_sci + phy_test)/6

passFail = False

if average_score < 35:
    grade = "F"
elif average_score < 50:
    grade = "D"
elif average_score < 60:
    grade = "C"
elif average_score <= 75:
    grade = "B"
    passFail = True
elif average_score <= 100:
    grade = "A"
    passFail = True

if passFail:
    print(f"Congratulations {student_name}!, you are passed and receive grade '{grade}'")
else:
    print(f"Sorry to say {student_name}, you are failed with grade {grade}")


"""
    2. Advanced Age Classifier

Categories: Infant (0-2), Child (3-12), Teen (13-19), Adult (20-64), Senior (65+)
Twist: Handle negative ages, ages >150, non-numeric input
Output different messages for each category

"""

age = int(input("To know the category, please enter the age :"))
if 0.1 < age < 2:
    print(f"As per age mentioned {age}, you are in Infant category.")
elif 3<= age <12:
    print(f"As per age mentioned {age}, you are a child")
elif 13 <= age < 19:
    print(f"As per age mentioned {age}, you a teenager!")
elif 20 <= age < 64:
    print(f"As per age mentioned {age}, you are n Adult")
elif 65 <= age < 150:
    print(f"As per age mentioned {age}, you are under Senior citizen category.")
else:
    print("Please mention the proper age in numberic value. e.g 10.")


"""
3. Shipping Cost Calculator

Weight-based pricing: <1kg=₹50, 1-5kg=₹100, 5-20kg=₹200, >20kg=₹500
Distance multiplier: Local(1x), State(1.5x), National(2x), International(3x)
Express delivery adds 50% to cost
Handle: Zero weight, invalid distance options

"""

print("Welcome to the Shipping Courier!")
weight = float(input("Please enter the weight of parcel (in Kg): "))
ship_distance = input("Where do you want to parcel the package? \n1. Local Transport 2. State Transport 3. National Transport 4. Internation Transport")
exp_delivery = input("Do you want to make it expresss delivery? ( you will be charged extra 50% of the total cost). 1. Yes 2. No")
ship_price = 0


if weight > 0:
    if weight < 1:
        ship_price += 50
    elif 1 <= weight < 5:
        ship_price += 100
    elif 5 <= weight < 20:
        ship_price += 200
    elif weight > 200:
        ship_price += 500
else:
    print("Sorry, we are not allowed to receive the wrong inputs. Weight cannot be 0 or negative.")

if ship_distance == "1" or ship_distance == "Local Transport":
    ship_price += ship_price
elif ship_distance == "2" or ship_distance == "State Transport":
    ship_price += (ship_price*1.5)
elif ship_distance == "3" or ship_distance == "National Transport":
    ship_price += (ship_price *2)
elif ship_distance == "4" or ship_distance =="International Transport":
    ship_price +=(ship_price *3)
else:
    print("Please provide proper input. Either mention proper option number or the text next to the option number.")


if exp_delivery == "Yes" or exp_delivery == "1":
    ship_price += (ship_price * 0.5)

print("Thank you for the inputs provided, your total shipping charges are INR-"+ str(ship_price)+ "only!")