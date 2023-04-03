yuan = float(input("what do u have left in yuan? "))
yen = float(input("what do u have left in yen? "))
won = float(input("what do u have left in won? "))

rta = (yuan*0.15) + (yen*0.0077) + (won*0.0008)
print(round(rta, 4)) #redondear 4 cifras después de la coma/punto