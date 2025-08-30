#================================ Exercise 001 ================================

print('Create a program that asks for your name and age, then prints "Hello [name], you are [age] years old!"')

name = input("Hello! May I know your name? :")
age = input("May I know your age as well? :")

print(f"Hello {name}, you are {age} years old!")

#================================ Exercise 002 ================================

print('Write a program that calculates and prints the number of days you\'ve been alive (assume 365 days per year).')


age = int(input("Hello, may I know your date of birth? :"))
total_years = 2025 - age
print(f"You are {total_years} years old. and you have been alive for {total_years * 365} days!")

#================================ Exercise 003 ================================

print("Create a simple band name generator that combines your pet's name and street name.")

name = input("Hello! May I know your name? : ")
pet_name = input("What is your pet's name? : ")

print(f"Your band name can be {name + pet_name}!")

#================================ Exercise 004 ================================

print("Write a program that takes a sentence as input and prints each word on a new line." )

inputLine = input("Hello, please mention the sentense: ")

words_lists = inputLine.split(" ")

for word in words_lists:
    print(word)


#================================ Exercise 005 ================================

print("Create a program that asks for your birth year and calculates what year you'll turn 100.")

birth_year = int(input("Please enter the birth year: "))

print(f"You will celebrate your 100th birthday in the year {birth_year + 100}!")

#================================ Exercise 006 ================================

print("Build a simple text formatter that takes a paragraph and prints it with each sentence on a new line")

long_text = input("Mention the paragraph: ")
# print("Reprinted the long text in line by line : \n " + str(long_text.split(".")))
sentences = long_text.split(". ")
for sentence in sentences:
    if sentence.strip():
        print(sentence.strip() + ".")


#================================ Exercise 007 ================================

print("Write a program that creates a simple ASCII art greeting with your name")

# no idea about ASCII and how to convert the character into ASCII.

name = input("Please enter your name: ")

print(f"""
 _   _      _ _       
| | | | ___| | | ___  
| |_| |/ _ \ | |/ _ \ 
|  _  |  __/ | | (_) |
|_| |_|\___|_|_|\___/ 

Hello {name}!
""")

#================================ Exercise 008 ================================

print("Create a program that generates a personalized fortune cookie message using your name and favorite number.")

name = input("Please enter your name: ")
number = int(input("Please enter your favourite number: "))

if number == 1:
    message = "you will have a great surprise today!"
elif number == 2:
    message = "your wish will come true soon!"
elif number == 3:
    message = "Success is on the horizon!"
elif number == 4:
    message = "You will find the missing piece to your puzzle!"
elif number == 5:
    message = "Brace yourself! An exciting opportunity is coming!"
elif number == 6:
    message = "Please consider the next step, you may get receive the big surprise!"
else:
    message = "Good luck will come your way!"

print(f"Hello {name}, you lucky number {number} says: {message}")

#================================ Exercise 009 ================================

print("Build a simple text-based business card generator that formats your information nicely.")

name = input("Can I have your full name?: ")

role = input("What's your profession/role?: ")

email_id= input("Can I have your email id?: ")

print(f"""

+-----------------------------------------------+
|     {name}                                    |
|     {role}                                    |
|     {email_id}                                |
+-----------------------------------------------+
      """)

#================================ Exercise 010 ================================

print('Write a program that takes your full name and creates a "cool" username by taking the first letter of your first name + your last name + your birth year.')

full_name = input("Enter your full name (First name, Last name):  ")

birth_year = input("Enter the birth year: ")

#print(f"Suggestion for your cool name is : {full_name[0] + full_name[1] + birth_year}")

first_name = full_name.split(" ")[0]
last_name = full_name.split(" ")[1]
print(f"Generated cool name is : {first_name[0] + last_name +birth_year}!")