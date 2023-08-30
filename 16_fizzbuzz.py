
for i in range(1, 101, 1):
    salida = ""
    if(i % 3 == 0):
        salida += "Fizz"
    if(i % 5 == 0):
        salida += "Buzz"
    
    if(salida == ""):
        print(i)
    else:
        print(salida)
        