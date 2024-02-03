import random
import math

def affirmation():
    gen =  random.randint(1,5)
    if gen == 1:
        print("I am in the right place, at the right time, doing the right thing.")
    elif gen == 2:
        print("I believe in myself.")
    elif gen == 3:
        print("I am kind to myself and others.")
    elif gen == 4:
        print("I accept myself exactly as I am without judgment.")
    else:
        print("I can do hard things.")

def abc():
    try:
        a = float(input("input value for a in ax^2 + bx + c = 0: "))
        b = float(input("input value for b in ax^2 + bx + c = 0: "))
        c = float(input("input value for c in ax^2 + bx + c = 0: "))
    except ValueError:
        print("not a valid number. try again")
        abc()
    if b ** 2 - 4 * a * c < 0:
        print("there are no real x intercepts for this input.")
    else:
        fx_int = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        sx_int = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        print(f"the first x intercept is: " + str(fx_int))
        print("the second x intercept is: " + str(sx_int))

affirmation()
abc()
