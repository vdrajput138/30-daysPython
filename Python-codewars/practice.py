#This code does not execute properly. Try to figure out why.
"""def multiply(a, b):
    a * b
"""

def multiply(a, b):
    return a * b


print(multiply(1,3))
print(multiply(2,3))
print(multiply(10,9))

#============================================================

"""
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
"""

def even_or_odd(number):
#    if number >= 0:
        if number %2 == 0:
            print("The number is Even number")
            return "Even"
        else:
            print("The number is Odd number")
            return "Odd"
#    else:
#        print("Please enter the positive number")

print(even_or_odd(-1))


#============================================================

"""Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
The correct answer would be 17.

"""
def count_sheeps(sheep):
    sheeps_count = 0
    for nums in sheep:
         if nums:
              sheeps_count += 1
    print(sheeps_count)


sheeps = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
count_sheeps(sheeps)
