
""" 
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
favourite_song = input("What is your favourite song? ")
artist_of_favourte_song = input("What is the artist of your favourite song? ")
song_duration = float(input("What is the duration of your favourite song? "))

output = f"Hello, {first_name} {last_name}, your favourite song is {favourite_song} by {artist_of_favourte_song}, and it's duration is {song_duration}!"

print(output) 
"""

"""
class Car:
    def __init__(any, wheels, colour, brand):
        any.wheels = wheels
        any.colour = colour
        any.brand = brand
    def drive(a):
        print("we be driving")
    def honkHorn(a):
        print("beep beep")


car1 = Car(4, "Silver", "Honda Jazz")
car2 = Car(6, "Pink", "BMW S Class")


print(car2.brand)

car1.honkHorn()
"""


"""
def add(x,y):
    z=x+y
    return(z)

def subtract(x,y):
    z=x-y
    return(z)

def multiply(x,y):
    z=x*y
    return(z)

def divide(x,y):
    z=x/y
    return(z)


print(divide(5,2))
"""

"""
a = int(input("Give the value of integer A: "))
b = int(input("Give the value of integer B: "))
c = int(input("Give the value of integer C: "))
if a > b and a > c:
    print("A is the largest number")
    if a == 0:
        print("and the largest number is equal to 0")
    if b > c:
        print("and C is the smallest number")
    elif c > b:
        print("and B is the smallest number")
    else:
        print("and B & C are equal")
elif b > a and b > c:
    print("B is the largest number")
    if b == 0:
        print("and the largest number is equal to 0")
    if a > c:
        print("and C is the smallest number")
    elif c > a:
        print("and A is the smallest number")
    else:
        print("and A & C are equal")
elif c > a and c > b:
    print("C is the largest number")
    if c == 0:
        print("and the largest number is equal to 0")
    if b > a:
        print("and A is the smallest number")
    elif a > b:
        print("and B is the smallest number")
    else:
        print("and A & B are equal")
elif a == b and a == c:
    print("All numbers are equal")
"""

"""
def countTo100():
    i=0
    while i <= 100:
        print(i)
        i+=5
    return()

def animals():
    count=0
    animalList = ["Cat","Dog","Rhino","Monkey","Tiger"]
    for i in animalList:
        count+=1
    print(count)
    return(count)

def incrementSelector():
    increment = int(input("What increment would you like to count by: "))
    i=0
    while i <= 1000 and i >= -1000:
        print(i)
        i+=increment
    return()

def fizzbuzz():
    i=0
    endPoint = int(input("Where would you like fizzbuzz to end: "))
    while i <= endPoint:
        if i % 5 == 0 and i % 3 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
        i+=1
    return()


def greetingsAndNames():
    greetings = ["Hello","Greetings","Good to see you","Fancy seeing you here","What's up","Hi"]
    names = ["John","Andrea","Stevenage","Gregoriovich","Rachmaninov","Maximal"]
    for i in greetings:
        for j in names:
            print(i + ", " + j)
"""
print("red" == "blue" or 5 < 3)