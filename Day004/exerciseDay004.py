import random
""" 
    1. Create a program that simulates rolling a dice (1-6) and tells the user if they got an even or odd number.
"""




""" 
    2. Write a program that picks a random item from a list of your 5 favorite foods and says "Today you should eat [food]!"
"""



""" 
    3. Build a simple coin flip simulator that randomly shows "Heads" or "Tails".
"""
coin_flip = random.randint(1,2)
if coin_flip == 1:
    coin_flipped = "Heads"
else:
    coin_flipped = "Tails"
user_guess = int(input("Guess the toss. 1. Heads 2. Tails"))


if user_guess == coin_flip:
    print("Congrats! You have guessed it right!")
else:
    print(f"Sorry it was {coin_flipped}!")

"""
    4. Create a "Random Compliment Generator" that picks from a list of 10 compliments and personalizes it with the user's name.
"""




"""
    5. Write a program that generates a random password using a list of characters (letters, numbers, symbols) - make it 6 characters long.
"""


"""
    6. Build a "What to Watch Tonight" program that randomly selects from different categories (Action, Comedy, Horror) and then picks a random movie from that category.
"""
cat = ["Action", "Horror", "Comedy","Thriller"]
amovies = ["A","B", "C"]
hmovies = ["D","E","F"]
cmovies = ["G","H","I"]
tmovies = ["J","K","L"]

catrandom = random.randint(1,4)
moviRandom = random.randint(1,3)
movieSelection = [];
if catrandom == 1:
    movieSelection = amovies
elif catrandom ==2:
    movieSelection = hmovies
elif catrandom == 3:
    movieSelection = cmovies
else:
    movieSelection = tmovies

print(f"Today, we wil watch {movieSelection[moviRandom-1]} from {cat[catrandom-1]} category")

"""
    7. Create a simple lottery number generator that picks 6 unique numbers between 1-49.
"""

print("Welcome to the lottery club! We are now starting to declare the lottery number sequence!")
num1 = random.randint(1,49)
print(f"Our First number is number {num1}")

num2 = random.randint(1,49)
print(f"Our First number is number {num2}")

num3 = random.randint(1,49)
print(f"Our First number is number {num3}")


num4 = random.randint(1,49)
print(f"Our First number is number {num4}")


num5 = random.randint(1,49)
print(f"Our First number is number {num5}")


num6 = random.randint(1,49)
print(f"Our First number is number {num6}")

print(f"Wow! our lottery sequence is - {num1} {num2} {num3} {num4} {num5} {num6}. Congratulations to the winner!")

"""
    8. Build a "Rock Paper Scissors" game where the computer randomly chooses and plays against the user.
"""


"""
    9. Create a "Daily Motivation Generator" that combines random motivational quotes with random goal suggestions.
"""



"""
    10. Write a program that creates a random study schedule - randomly assigns 5 subjects to 5 different time slots.
"""