print("Welcome to the Cyclone, the best NY city rollercoaster!")
height = float(input("What's your height? (cm)"))
credits = int(input("How many credits do you have? "))

if height >= 137 and credits >= 10:
    print("Enjoy the ride!!")
elif height < 137:
    print("I'm sorry, you're not tall enough to ride")
elif credits < 10:
    print("Ups, you don't have enough credits to ride")
else:
    print("Invalid data")
