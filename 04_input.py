import random

user_name = (input('Please, enter your name: '))
print(f"Hello, {user_name}")

user_age = int(input('Now, what\'s your age: '))
greetings = ["Hi", "Yo!", "Ahoy", "What's up!", "Hello", "Hey"]
if(user_age >= 25 and user_age <= 50): 
    print("Hello fossil =)")
else: print(random.choice(greetings))

"""otras opciones para seleccion random/secrets
random.SystemRandom() 
random.SystemRandom().sample(lista, #) -> selecciona más de 1 element random"""
