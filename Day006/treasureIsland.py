print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

answer1 = input("You're at a cross road. Where do you want to go? (Left or Right?): ")
if answer1 == "Left":
    answer2 = input("Great choice! Will you wait for a boat or you will cross the river by swimming through it?(Wait or Swim): ")
    if answer2 =="Wait":
        answer3 = input("Clever thinking! You have reached to the castle! \nAt the front, you can see 4 doors. Red colored, Blue colored, Black colored and Yellow Colored. \nWhich one will you choose to enter in castle?(Red, Blue,Black,Yellow): ")
        if answer3 == "Black":
            print("You dropped in a cage.Game Over!")
        elif answer3 == "Red":
            print("You were burnt by Fire, Game Over!")
        elif answer3 == "Blue":
            print("You've been eaten by beasts, Game Over!")
        elif answer3 == "Yellow":
            print("Awesome! You've won! Congratulations!")
    else:
        print("You've been attacked by piranhas, Game Over!")
else:
    print("You fell into a hole! Game Over")
