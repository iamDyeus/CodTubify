import random

def greet():
    greetings = ['Hola !', 'Hello :)', 'Sup '+("\U0001f60e"), 'Howdy '+ ("\U0001F607"), 'Greetings !',  'Ola !' , 'Allo !']
    return random.choice(greetings)
