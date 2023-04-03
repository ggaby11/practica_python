gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

question_one = int(input("Q1) Do you like Dawn or Dusk? \n    1) Dawn\n    2) Dusk\n"))

if question_one > 2:
  print("Wrong input.")
elif question_one == 2:
  hufflepuff += 1
  slytherin += 1
else:
  gryffindor += 1
  ravenclaw += 1

question_two = int(input("Q2) When I'm dead, I want people to remember me as: ? \n    1) The Dood\n    2) The Great\n    3) The Wise\n    4) The Bold\n"))

if question_two > 4:
  print("Wrong input.")
elif question_two == 4:
  gryffindor += 2
elif question_two == 3:
  ravenclaw += 2
elif question_two == 2:
  slytherin += 2
else: 
  hufflepuff += 2

question_three = int(input("Q3) Wich kind of instrument most pleases your ear? \n    1) The violin\n    2) The trumpet\n    3) The piano\n    4) The drum\n"))

if question_three > 4:
  print("Wrong input.")
elif question_three == 4:
  gryffindor += 4
elif question_three == 3:
  ravenclaw += 4
elif question_three == 2:
  hufflepuff += 4
else: 
  slytherin += 4

if gryffindor > ravenclaw and ravenclaw > hufflepuff and hufflepuff > slytherin:
  print(f"gryffindor ({gryffindor})")
elif ravenclaw > hufflepuff and hufflepuff > slytherin:
  print(f"ravenclaw ({ravenclaw})")
elif hufflepuff > slytherin:
  print(f"hufflepuff ({hufflepuff})")
else: 
  print(f"slytherin ({slytherin})")
