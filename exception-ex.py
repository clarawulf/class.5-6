#1
try:
    age = int(input("What is your age?"))
except ValueError:
    print("I am sorry, but that is not a valid number")
else:
    print("Your age is", age)
#2
try:
    age1 = int(input("What is your age player 1? "))
    age2 = int(input("What is your age player 2? "))
    res = age1/age2
except ValueError:
    print("I am sorry, but that is not a valid number")
else:
    print("Player 1 is older than player 2 by a factor of", res)
#3
try:
    age1 = int(input("What is your age player 1? "))
    age2 = int(input("What is your age player 2? "))
    res = age1/age2
except ValueError:
    print("I am sorry, but that is not a valid number")
except ZeroDivisionError:
    print("I am sorry, but you cannot divide by zero")
except:
    print("I am sorry, but something went wrong")
else:
    print("Player 1 is older than player 2 by a factor of", res)
finally:
    print("Thank you for playing!")

#you always start with a try
#then add the exceptions that could arrive
#only one "else", optional
#finally, end of the try block, happens no matter the outcome 