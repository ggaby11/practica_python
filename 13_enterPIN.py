print("WELCOME TO BANK OF CODEDEX")

pin = int(input("Enter your PIN: "))

while pin != 1234:
  pin = int(input ("Incorrect PIN. Enter your PIN again: "))

print("PIN accepted!")