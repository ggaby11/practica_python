print("\nWelcome to the Cyclone, the best NY city rollercoaster! \nPlease answer the next questions to determine if you can enter...")
height = float(input("\nWhat's your height? (cm) "))
credits = int(input("How many credits do you have? "))

with_taller_person = str(input("Are you with a taller person? (y/n) "))

if with_taller_person == 'y':
    with_taller_person = True
else: with_taller_person = False

if (height >= 137 and credits >= 10) or (height >= 100 and with_taller_person):
    print("Enjoy the ride!!")
elif (height < 137):
    print("I'm sorry, you're not tall enough to ride")
elif credits < 10:
    print("Ups, you don't have enough credits to ride")
else:
    print("Invalid data")
