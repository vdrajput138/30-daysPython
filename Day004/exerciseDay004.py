import random

""" 
    1. Create a program that simulates rolling a dice (1-6) and tells the user if they got an even or odd number.
"""

print("Welcome to the number with rolling dice!")
rolledDice = random.randint(1, 6)
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
toss = ["Heads", "Tails"]
coin_flip = random.choice(toss)
user_guess = input("Guess the toss. \nHeads or Tails? : ")


if user_guess == coin_flip:
    print("Congrats! You have guessed it right!")
else:
    print(f"Sorry it was {coin_flip}!")

"""
    4. Create a "Random Compliment Generator" that picks from a list of 10 compliments and personalizes it with the user's name.
"""

compliments = [
    "Your kindness is contagious.",
    "Your smile could power a small city.",
    "You have an amazing sense of humor.",
    "If you were a vegetable, you’d be a cute-cumber.",
    "Your confidence is inspiring.",
    "You’re like a human Swiss Army knife – prepared for anything!",
    "You’re an exceptional problem-solver.",
    "Your dance moves are so smooth, butter is jealous.",
    "Your creativity knows no bounds.",
    "You’re the human equivalent of a perfect cup of coffee.",
]
nameip = input("Hello, may I know your name? ")
print(f"Hello, {nameip}! {random.choice(compliments)}")

"""
    5. Write a program that generates a random password using a list of characters (letters, numbers, symbols) - make it 6 characters long.
"""
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%^&*()_+-={}[];':,.\\/\""
combination = letters + numbers + symbols
print(f"You can use the password as {''.join(random.sample(combination,k=8))}")


"""
    6. Build a "What to Watch Tonight" program that randomly selects from different categories (Action, Comedy, Horror) and then picks a random movie from that category.
"""
cat = ["Action", "Horror", "Comedy", "Thriller"]
amovies = ["A", "B", "C"]
hmovies = ["D", "E", "F"]
cmovies = ["G", "H", "I"]
tmovies = ["J", "K", "L"]

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

print(
    "Welcome to the lottery club! We are now starting to declare the lottery number sequence!"
)
print(f"Congratulation! The number is {random.sample(range(1,50),6)}")


"""
    8. Build a "Rock Paper Scissors" game where the computer randomly chooses and plays against the user.
"""

pickOne = random.choice(["Rock", "Paper", "Scissor"])
userIp = input(
    "Welcome to the the game of Rock, Paper, Scissor! \n What would you like to choose? \n Rock, Paper or Scissor?: "
)

if pickOne == userIp:
    print("Its a draw!")
elif (
    (pickOne == "Paper" and userIp == "Rock")
    or (pickOne == "Scissor" and userIp == "Paper")
    or (pickOne == "Rock" and userIp == "Scissor")
):
    print("You Lost.")
elif (
    (pickOne == "Paper" and userIp == "Scissor")
    or (pickOne == "Rock" and userIp == "Paper")
    or (pickOne == "Scissor" and userIp == "Rock")
):
    print("You've Won!")


"""
    9. Create a "Daily Motivation Generator" that combines random motivational quotes with random goal suggestions.
"""
goal_suggestions = [
    "Learn a new skill, like a language or instrument.",
    "Improve your mindset and develop a growth mindset.",
    "Practice mindfulness or meditation daily.",
    "Embrace self-care routines, such as a self-care morning or Sunday.",
    "Become a better listener.",
    "Read a certain number of books per year.",
    "Write a book or start a creative project.",
    "Journal or use a planner.",
    "Expand your professional network.",
    "Develop a new hard skill, such as a programming language.",
    "Earn a new professional certification.",
    "Find a mentor or become one.",
    "Find a career you love.",
    "Learn to make effective decisions.",
    "Adopt a healthier lifestyle, like biking to work.",
    "Improve your eating habits, such as trying a new cuisine monthly.",
    "Go for walks every day.",
    "Improve your self-esteem and attend more social events.",
    "Create a family fun day and make it a tradition.",
]

quotes = [
    "“Success is not final; failure is not fatal: It is the courage to continue that counts.” —Winston Churchill",
    "“It is better to fail in originality than to succeed in imitation.” —Herman Melville",
    "“The road to success and the road to failure are almost exactly the same.” —Colin R. Davis",
    "“Success usually comes to those who are too busy to be looking for it.” —Henry David Thoreau",
    "“Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.” —Dale Carnegie",
    "“Nothing in the world can take the place of persistence. Talent will not; nothing is more common than unsuccessful men with talent. Genius will not; unrewarded genius is almost a proverb. Education will not; the world is full of educated derelicts. The slogan ’Press On’ has solved and always will solve the problems of the human race.” —Calvin Coolidge",
    "“There are three ways to ultimate success: The first way is to be kind. The second way is to be kind. The third way is to be kind.” —Mister Rogers",
    "“Success is peace of mind, which is a direct result of self-satisfaction in knowing you made the effort to become the best of which you are capable.” —John Wooden",
    "“I never dreamed about success. I worked for it.” —Estée Lauder",
    "“Success is getting what you want; happiness is wanting what you get.” ―W. P. Kinsella",
    "“It is remarkable how much long-term advantage people like us have gotten by trying to be consistently not stupid instead of trying to be very intelligent.” —Charlie Munger",
    "“You can't be that kid standing at the top of the waterslide, overthinking it. You have to go down the chute.” —Tina Fey",
    "“When I believe in something, I'm like a dog with a bone.” —Melissa McCarthy",
    "“And the day came when the risk to remain tight in a bud was more painful than the risk it took to blossom.” —Anaïs Nin",
    "“The standard you walk past is the standard you accept.” —David Hurley",
    "“I've searched all the parks in all the cities and found no statues of committees.” —Gilbert K. Chesterton",
    "“Success is stumbling from failure to failure with no loss of enthusiasm.” ―Winston Churchill",
    "“Keep your eyes on the stars and your feet on the ground.” ―Theodore Roosevelt",
    "“Do not stop thinking of life as an adventure. You have no security unless you can live bravely, excitingly, imaginatively; unless you can choose a challenge instead of competence.” ―Eleanor Roosevelt",
    "“Perfection is not attainable. But if we chase perfection we can catch excellence.” —Vince Lombardi",
    "“Get a good idea and stay with it. Dog it, and work at it until it's done right.” —Walt Disney",
    "“Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence.” —Helen Keller",
    "“The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty.” —Winston Churchill",
    "“Don't let yesterday take up too much of today.” —Will Rogers",
    "“You learn more from failure than from success. Don't let it stop you. Failure builds character.” —Unknown",
    "“If you are working on something that you really care about, you don't have to be pushed. The vision pulls you.” —Steve Jobs",
    "“Experience is a hard teacher because she gives the test first, the lesson afterward.” ―Vernon Sanders Law",
    "“To know how much there is to know is the beginning of learning to live.” —Dorothy West",
    "“Goal setting is the secret to a compelling future.” —Tony Robbins",
]


print(
    f"Today's Quote - {random.choice(quotes)} and your goal suggestion is - {random.choice(goal_suggestions)}"
)


"""
    10. Write a program that creates a random study schedule - randomly assigns 5 subjects to 5 different time slots.
"""

subjects = ["Maths", "English", "History", "Geography", "Politics", "Grammer"]
time_slots = ["10-11 am", "12-1pm", "3-4pm", "5-6pm", "7-8pm", "9-10am"]

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

warm_colors = [
    "light blue",
    "Light green",
    "Light gold",
    "yellow",
    "light orange",
    "light grey",
]
cool_colors = ["cyan", "sky blue", "light blue", "silver", "light pink", "light green"]
natural_colors = ["red", "blue", "green", "pink", "black", "purple"]

arr_colors = [warm_colors, cool_colors, natural_colors]

random_choice = random.choice(arr_colors)

list_of_colors = random.sample(random_choice, 5)

print(list_of_colors)


"""
12. Random Workout Generator

Lists: upper_body_exercises, lower_body_exercises, cardio_exercises
Generate a 7-exercise routine with exactly 2 from each category + 1 random bonus
No exercise should repeat

"""

upper_body_exercise = [
    "exercise 1",
    "exercise 2",
    "exercise 3",
    "exercise 4",
    "exercise 5",
]

lower_body_exercise = [
    "exercise 6",
    "exercise 7",
    "exercise 8",
    "exercise 9",
    "exercise 10",
]

cardio_exercise = [
    "exercise 11",
    "exercise 12",
    "exercise 13",
    "exercise 14",
    "exercise 15",
]

bonus_exercise = ["exercise 16", "exercise 17", "exercise 18"]

two_samples_lower = random.sample(lower_body_exercise, 2)
two_samples_upper = random.sample(upper_body_exercise, 2)
two_samples_cardio = random.sample(cardio_exercise, 2)
sample_bonus = random.choice(bonus_exercise)

print(
    f"These exercise you can perform for this week - {two_samples_lower}, {two_samples_upper},{two_samples_cardio} and one bonus {sample_bonus}"
)


"""
13. Random Playlist Creator

4 genre lists: rock, pop, classical, jazz (5 songs each)
Create 8-song playlist with at least 1 song from each genre
Remaining 4 songs can be from any genre, but no duplicates
"""
rock_songs = [
    "rock and roll",
    "Highway to hell",
    "Pink",
    "hero",
    "born to fly",
    "just do it",
]
pop_songs = [
    "britney bitch",
    "ketty perry",
    "kiss the girl",
    "friday night",
    "taylor swift",
    "adele",
]
classical_songs = [
    "jazz_song",
    "flute_song",
    "armin_nonbase",
    "noor",
    "lata ji",
    "base_songs",
]
jazz_songs = ["song1", "song2", "song3", "song4", "song5", "song6"]

rock_sample = random.choice(rock_songs)
rock_songs.remove(rock_sample)

pop_sample = random.choice(pop_songs)
pop_songs.remove(pop_sample)

classical_sample = random.choice(classical_songs)
classical_songs.remove(classical_sample)

jazz_sample = random.choice(jazz_songs)
jazz_songs.remove(jazz_sample)

all_songs = rock_songs + pop_songs + classical_songs + jazz_songs
remaining_songs = random.sample(all_songs, 4)

remaining_songs_strings = ", ".join(remaining_songs)

print(
    f"Your playlist for today is {rock_sample}, {pop_sample}, {classical_sample}, {jazz_sample} and the remaining songs are {remaining_songs_strings}"
)


"""
14. Random Recipe Ingredient Substitution

Original recipe list: ["flour", "eggs", "milk", "sugar", "butter"]
Substitution options for each ingredient (nested lists)
Randomly substitute 2-3 ingredients and show the new recipe
"""
og_recipe_list = ["flour", "eggs", "milk", "sugar", "butter"]
og_recipe_list_string = ", ".join(og_recipe_list)
alt_options = [["opt_flour1","opt_flour2","opt_flour3","opt_flour4"],["opt_eggs1","opt_eggs2","opt_eggs3","opt_eggs4"],["opt_milk1","opt_milk2","opt_milk3","opt_milk4"],["opt_sugar1","opt_sugar2","opt_sugar3","opt_sugar4"],["opt_butter1","opt_butter2","opt_butter3","opt_butter4"]]

to_replace_ingredients = random.sample(og_recipe_list, k=random.randint(2,3))
for item in to_replace_ingredients:
    # ingredient_replace = random.choice(og_recipe_list)
    position_of_ingredient = og_recipe_list.index(item)
    replaced_ingredient = random.choice(alt_options[position_of_ingredient])
    og_recipe_list[position_of_ingredient] = replaced_ingredient

modified_og_recipe_list_string = ", ".join(og_recipe_list)

print(f"We had a original receipe ingredients as {og_recipe_list_string} which we updated by switching few ingredeints {modified_og_recipe_list_string}")


"""
15. Random Tournament Bracket Generator

List of 8 player names
Create random matchups for first round (4 pairs)
Simulate random winners to create final bracket
No player should play themselves
"""
players_list = ["p1","p2","p3","p4","p5","p6","p7","p8"]

random.shuffle(players_list)


list_of_chunks = [
[players_list[0], players_list[1]],
[players_list[2], players_list[3]],
[players_list[4], players_list[5]],
[players_list[6], players_list[7]]]

print(f"Here's the random selection - {random.sample(list_of_chunks,1)}")


"""
16. Random Escape Room Puzzle

3 rooms, each with 3-4 random clues from different clue pools
Player picks a room, gets random clues, must solve to "escape"
Track which clues were used (no repeats across rooms)
"""
room1_clue = ["check the door latch", "check the hanging wall","tap the rung","check the window","hit the wall"]
room2_clue = ["remove the painting","slide the door","push the wall","tilt the wall clock","turn on the fan"]
room3_clue =["key is under the mat","dragh down the latch of hanging piece","pull down the bedroom rope","slide the bed"]

room_selection = int(input("Please select the room you want to enter. \n1. Room 1 \t2. Room 2 \t3.Room 3. : "))
random_clue = ""
if room_selection == 1:
    random_clue = random.choice(room1_clue)
elif room_selection ==2:
    random_clue = random.choice(room2_clue)
elif room_selection == 3:
    random_clue = random.choice(room3_clue)
else:
    print("Please mention either 1,2 or 3. You have entered invalid input.")

print(f"You have selected room {room_selection} and here's a clue to escape from room - {random_clue}")

"""
17. Random Shopping List Optimizer

Categories: produce, dairy, meat, pantry, frozen
Randomly generate 12 items across categories
Sort them by optimal shopping path (produce→dairy→meat→pantry→frozen)
"""
produce = [1,2,3,4,5,6,7,8,9,10]
meat = [11,12,13,14,15,16,17,18,19,20]
dairy = [21,22,23,24,25,26,27,28,29,30] 
pantry = [31,32,33,34,35,36,37,38,39,40]
frozen = [41,42,43,44,45,46,47,48,49,50]

combined_products = produce + meat + dairy + pantry + frozen
print(combined_products)
selected_random = random.sample(combined_products,12)
print(selected_random)
#TODO - Complete this task after learning tuples and directory 

"""
18. Random Language Learning Flashcards

20 English words with translations in 3 languages
Randomly select 5 words and random target language
Quiz format with random order, track score
"""
words = ["Hi","Mango","Man","Woman","Wood", "Tree", "Sunrise", "Dawn","Clever"]
hindi_translation = ["namste","Aam","Insaan","Aurat","Lakdi","Ped","suryoday","Sham","hoshiyar"]
marathi_translation =["namaskar","Amba","Manus","Bai","Lakud","Jhad","Suryoday","Sandhyakal","Hushar"]

sample_random_words = random.sample(words,5)

for i in sample_random_words:
    index_of_word = words.index(i)
    langugae_selection = random.choice(range(0,1))
    if langugae_selection == 0:
        translated_meaning = hindi_translation[index_of_word]
    else:
        translated_meaning = marathi_translation[index_of_word]
    print(f"We have a random word as {i} and its meaning in {"Hindi" if langugae_selection ==0 else "Marathi"} is {translated_meaning}")

"""
Advanced Logic Exercises (16-20):




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
