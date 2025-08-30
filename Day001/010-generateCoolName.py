print('Write a program that takes your full name and creates a "cool" username by taking the first letter of your first name + your last name + your birth year.')

full_name = input("Enter your full name (First name, Last name):  ")

birth_year = input("Enter the birth year: ")

print(f"Suggestion for your cool name is : {full_name[0] + full_name[1] + birth_year}")