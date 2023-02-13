import random
question = str(input("Question: "))
random_number = random.randint(1,9)

if random_number >= 9:
  rta = ("Yes - definitely.")
elif random_number >= 8:
  rta = ("It is decidedly so.")
elif random_number >= 7:
  rta = ("Without a doubt.")
elif random_number >= 6:
  rta = ("Reply hazy, try again.")
elif random_number >= 5:
  rta = ("Ask again later.")
elif random_number >= 4:
  rta = ("Better not tell you now.")
elif random_number >=3:
  rta = ("My sources say no.")
elif random_number >= 2:
  rta = ("Error.")
else:
  rta = ("Very doubtful.")

print("\nQuestion: " + question)
print("Magic 8 ball: " + rta)