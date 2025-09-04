"""1. Grade Calculator (Enhanced)

Input: Multiple subject marks (at least 5 subjects)
Calculate average, assign letter grade, determine if student passes (>60%)
Handle invalid marks, divide by zero

2. Advanced Age Classifier

Categories: Infant (0-2), Child (3-12), Teen (13-19), Adult (20-64), Senior (65+)
Twist: Handle negative ages, ages >150, non-numeric input
Output different messages for each category

3. Shipping Cost Calculator

Weight-based pricing: <1kg=₹50, 1-5kg=₹100, 5-20kg=₹200, >20kg=₹500
Distance multiplier: Local(1x), State(1.5x), National(2x), International(3x)
Express delivery adds 50% to cost
Handle: Zero weight, invalid distance options

4. Restaurant Ordering System

Menu: Starter(₹200), Main(₹500), Dessert(₹150), Drink(₹100)
Discounts: >₹1000 = 10% off, >₹1500 = 15% off, >₹2000 = 20% off
Tax: 18% GST after discount
Handle: Invalid menu choices, empty orders

5. Password Strength Checker

Requirements: 8+ chars, 1 uppercase, 1 lowercase, 1 number, 1 special char
Output: Weak/Medium/Strong with specific feedback
Handle: Empty strings, spaces only"""



"""
    Grade Calculator
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