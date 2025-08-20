len("12345")

#typechecking
print(type("Hello"))
print(type(12345))
print(type(123_456_789))
print(type(123.456))
print(type(True))


print(type(len("12345")))


#Type Conversion

#convert string into int
print(int("123") + int("456"))
#print(int("abc") + int("456"))  ValueError: invalid literal for int() with base 10: 'abc'


#print("Number of letters in your name: " + len(input("Enter your name"))) TypeError: can only concatenate str (not "int") to str

print("Number of letters in your name: " + str(len(input("Enter your name"))))