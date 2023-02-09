print('Hola Mundo')#comillas simples
print("Hola Mundo\n")#comillas dobles

"""
Usar comillas simples o dobles
es lo mismo en python.
"""

'''
Las variables no se declaran
se le asignan valores, ejemplo con 
diff tipos de datos:
'''
texto = "Holaa"
numero_entero = 30
numero_decimal = 1.27
boolean = False #primera letra en mayus -True -False
lista = [2, 4, 6, 8] #datos ordenados que pueden cambiar
diccionario = {'saludo' : 'hola', 'despedida' : ['adios','hasta luego', 'chao'], 'hora' : 13, 'am' : False} #pueden trabajar varios datos y en varias cantidades
tupla = ('1', '2', '3', '4', '5', '6', '7', '8', '9') #datos ordenados que no cambian
set = {1.5, 2, '12', 2.5, "holis"} #datos no ordenados

print(f"texto: {type(texto)} \nnumero_entero: {type(numero_entero)} \nnumero_decimal: {type(numero_decimal)} \n")
print(f"boolean: {type(boolean)} \ndiccionario: {type(diccionario)} \n")
print(f"lista: {type(lista)} \ntupla: {type(tupla)} \nset: {type(set)} \n")