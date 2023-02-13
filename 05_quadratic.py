a = float(input('Enter a:'))
b = float(input('Enter b:'))
c = float(input('Enter c:'))

ecuacion = pow((b*b - 4*a*c), 0.5)
print(ecuacion)
root1 = (-b + ecuacion) / (a*2)
root2 = (-b - ecuacion) / (a*2)

print(f"root1: {root1} \nroot2: {root2}")