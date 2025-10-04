import random
""" 
    1. Create a program that simulates rolling a dice (1-6) and tells the user if they got an even or odd number.
"""

print("Welcome to the number with rolling dice!")
rolledDice = random.randint(1,6)
evenOrOdd = "undefined"
if rolledDice % 2 == 0:
    evenOrOdd = "Even"
else:
    evenOrOdd = "Odd"
print(f"Wow! The rolled number is {rolledDice} and it's a {evenOrOdd} number.")


""" 
    2. Write a program that picks a random item from a list of your 5 favorite foods and says "Today you should eat [food]!"
"""

listOfFavFoods = ["Banana", "Apple", "Watermelon", "Sapota", "Kiwi"]
# numberSel = random.randint(0,4)
print(f"Today you should eat {random.choice(listOfFavFoods)}")



""" 
    3. Build a simple coin flip simulator that randomly shows "Heads" or "Tails".
"""
toss = ["Heads","Tails"]
coin_flip = random.choice(toss)
user_guess = input("Guess the toss. \nHeads or Tails? : ")


if user_guess == coin_flip:
    print("Congrats! You have guessed it right!")
else:
    print(f"Sorry it was {coin_flip}!")

"""
    4. Create a "Random Compliment Generator" that picks from a list of 10 compliments and personalizes it with the user's name.
"""

compliments = ["Your kindness is contagious.", "Your smile could power a small city.", "You have an amazing sense of humor.", "If you were a vegetable, you’d be a cute-cumber.", "Your confidence is inspiring.", "You’re like a human Swiss Army knife – prepared for anything!", "You’re an exceptional problem-solver.", "Your dance moves are so smooth, butter is jealous." , "Your creativity knows no bounds." , "You’re the human equivalent of a perfect cup of coffee."]
nameip = input("Hello, may I know your name? ")
print(f"Hello, {nameip}! {random.choice(compliments)}")

"""
    5. Write a program that generates a random password using a list of characters (letters, numbers, symbols) - make it 6 characters long.
"""
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%^&*()_+-={}[];':,.\\/\""
combination = letters+numbers+symbols
print(f"You can use the password as {''.join(random.sample(combination,k=8))}")


"""
    6. Build a "What to Watch Tonight" program that randomly selects from different categories (Action, Comedy, Horror) and then picks a random movie from that category.
"""
cat = ["Action", "Horror", "Comedy","Thriller"]
amovies = ["A","B", "C"]
hmovies = ["D","E","F"]
cmovies = ["G","H","I"]
tmovies = ["J","K","L"]

catrandom = random.choice(cat)
if catrandom == "Action":
    movieSelection = random.choice(amovies)
elif catrandom == "Horror":
    movieSelection = random.choice(hmovies)
elif catrandom == "Comedy":
    movieSelection = random.choice(cmovies)
else:
    movieSelection = random.choice(tmovies)

print(f"Today, we wil watch {movieSelection} from {catrandom} category")


"""
    7. Create a simple lottery number generator that picks 6 unique numbers between 1-49.
"""

print("Welcome to the lottery club! We are now starting to declare the lottery number sequence!")
print(f"Congratulation! The number is {random.sample(range(1,50),6)}")


"""
    8. Build a "Rock Paper Scissors" game where the computer randomly chooses and plays against the user.
"""

pickOne = random.choice(["Rock", "Paper", "Scissor"]) 
userIp = input("Welcome to the the game of Rock, Paper, Scissor! \n What would you like to choose? \n Rock, Paper or Scissor?: ")

if pickOne == userIp:
    print("Its a draw!")
elif (pickOne == "Paper" and userIp == "Rock") or (pickOne == "Scissor" and userIp == "Paper") or (pickOne == "Rock" and userIp == "Scissor"):
    print("You Lost.")
elif (pickOne == "Paper" and userIp == "Scissor") or (pickOne == "Rock" and userIp == "Paper") or (pickOne == "Scissor" and userIp == "Rock"):
    print("You've Won!")


"""
    9. Create a "Daily Motivation Generator" that combines random motivational quotes with random goal suggestions.
"""
goal_suggestions = ["Learn a new skill, like a language or instrument.",
"Improve your mindset and develop a growth mindset.", "Practice mindfulness or meditation daily.",
"Embrace self-care routines, such as a self-care morning or Sunday.", "Become a better listener.",
"Read a certain number of books per year.", "Write a book or start a creative project.", "Journal or use a planner.",
"Expand your professional network.", "Develop a new hard skill, such as a programming language.", 
"Earn a new professional certification.", "Find a mentor or become one.", "Find a career you love.", 
"Learn to make effective decisions.", "Adopt a healthier lifestyle, like biking to work.", 
"Improve your eating habits, such as trying a new cuisine monthly.", "Go for walks every day.", 
"Improve your self-esteem and attend more social events.", "Create a family fun day and make it a tradition."]

quotes = ['“Success is not final; failure is not fatal: It is the courage to continue that counts.” —Winston Churchill',
'“It is better to fail in originality than to succeed in imitation.” —Herman Melville',
'“The road to success and the road to failure are almost exactly the same.” —Colin R. Davis',
'“Success usually comes to those who are too busy to be looking for it.” —Henry David Thoreau', 
'“Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.” —Dale Carnegie',
'“Nothing in the world can take the place of persistence. Talent will not; nothing is more common than unsuccessful men with talent. Genius will not; unrewarded genius is almost a proverb. Education will not; the world is full of educated derelicts. The slogan ’Press On’ has solved and always will solve the problems of the human race.” —Calvin Coolidge',
'“There are three ways to ultimate success: The first way is to be kind. The second way is to be kind. The third way is to be kind.” —Mister Rogers',
'“Success is peace of mind, which is a direct result of self-satisfaction in knowing you made the effort to become the best of which you are capable.” —John Wooden',
'“I never dreamed about success. I worked for it.” —Estée Lauder',
'“Success is getting what you want; happiness is wanting what you get.” ―W. P. Kinsella',
'“It is remarkable how much long-term advantage people like us have gotten by trying to be consistently not stupid instead of trying to be very intelligent.” —Charlie Munger',
'“You can\'t be that kid standing at the top of the waterslide, overthinking it. You have to go down the chute.” —Tina Fey',
'“When I believe in something, I\'m like a dog with a bone.” —Melissa McCarthy',
'“And the day came when the risk to remain tight in a bud was more painful than the risk it took to blossom.” —Anaïs Nin',
'“The standard you walk past is the standard you accept.” —David Hurley',
'“I\'ve searched all the parks in all the cities and found no statues of committees.” —Gilbert K. Chesterton',
'“Success is stumbling from failure to failure with no loss of enthusiasm.” ―Winston Churchill',
'“Keep your eyes on the stars and your feet on the ground.” ―Theodore Roosevelt',
'“Do not stop thinking of life as an adventure. You have no security unless you can live bravely, excitingly, imaginatively; unless you can choose a challenge instead of competence.” ―Eleanor Roosevelt',
'“Perfection is not attainable. But if we chase perfection we can catch excellence.” —Vince Lombardi',
'“Get a good idea and stay with it. Dog it, and work at it until it\'s done right.” —Walt Disney',
'“Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence.” —Helen Keller',
'“The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty.” —Winston Churchill',
'“Don\'t let yesterday take up too much of today.” —Will Rogers',
'“You learn more from failure than from success. Don\'t let it stop you. Failure builds character.” —Unknown',
'“If you are working on something that you really care about, you don\'t have to be pushed. The vision pulls you.” —Steve Jobs',
'“Experience is a hard teacher because she gives the test first, the lesson afterward.” ―Vernon Sanders Law',
'“To know how much there is to know is the beginning of learning to live.” —Dorothy West',
'“Goal setting is the secret to a compelling future.” —Tony Robbins']


print(f"Today's Quote - {random.choice(quotes)} and your goal suggestion is - {random.choice(goal_suggestions)}")


"""
    10. Write a program that creates a random study schedule - randomly assigns 5 subjects to 5 different time slots.
"""

subjects = ["Maths","English","History","Geography","Politics","Grammer"]
time_slots = ["10-11 am","12-1pm", "3-4pm", "5-6pm", "7-8pm", "9-10am"]

random.shuffle(subjects)
random.shuffle(time_slots)

print(f"On {time_slots[0]} - subject is {subjects[0]}")
print(f"On {time_slots[1]} - subject is {subjects[1]}")
print(f"On {time_slots[2]} - subject is {subjects[2]}")
print(f"On {time_slots[3]} - subject is {subjects[3]}")
print(f"On {time_slots[4]} - subject is {subjects[4]}")
print(f"On {time_slots[5]} - subject is {subjects[5]}")


""""
11. Random Color Palette Generator

Create 3 lists: warm_colors, cool_colors, neutral_colors
Randomly pick one category, then select 5 colors from that category
Ensure no duplicate colors in final palette

"""

warm_colors = ["light blue","Light green", "Light gold","yellow","light orange","light grey"]
cool_colors = ["cyan","sky blue","light blue","silver","light pink","light green"]
natural_colors = ["red","blue","green","pink","black","purple"]

arr_colors = [warm_colors, cool_colors,natural_colors]

random_choice = random.choice(arr_colors)

list_of_colors = random.sample(random_choice,5) 

print(list_of_colors)



"""


12. Random Workout Generator

Lists: upper_body_exercises, lower_body_exercises, cardio_exercises
Generate a 7-exercise routine with exactly 2 from each category + 1 random bonus
No exercise should repeat

13. Random Playlist Creator

4 genre lists: rock, pop, classical, jazz (5 songs each)
Create 8-song playlist with at least 1 song from each genre
Remaining 4 songs can be from any genre, but no duplicates

14. Random Recipe Ingredient Substitution

Original recipe list: ["flour", "eggs", "milk", "sugar", "butter"]
Substitution options for each ingredient (nested lists)
Randomly substitute 2-3 ingredients and show the new recipe

15. Random Tournament Bracket Generator

List of 8 player names
Create random matchups for first round (4 pairs)
Simulate random winners to create final bracket
No player should play themselves

Advanced Logic Exercises (16-20):
16. Random Escape Room Puzzle

3 rooms, each with 3-4 random clues from different clue pools
Player picks a room, gets random clues, must solve to "escape"
Track which clues were used (no repeats across rooms)

17. Random Shopping List Optimizer

Categories: produce, dairy, meat, pantry, frozen
Randomly generate 12 items across categories
Sort them by optimal shopping path (produce→dairy→meat→pantry→frozen)

18. Random Language Learning Flashcards

20 English words with translations in 3 languages
Randomly select 5 words and random target language
Quiz format with random order, track score

19. Random Weather-Based Activity Suggester

Weather conditions list: sunny, rainy, snowy, cloudy, windy
Activity lists for each weather type
Randomly pick weather + activity, but add constraints (no swimming when cold)

20. Random Group Project Assigner

15 student names, 5 different project types
Create 3 groups of 5 students each
Randomly assign project types ensuring balanced skill distribution
"""