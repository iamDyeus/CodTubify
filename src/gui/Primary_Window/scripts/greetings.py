import random

def greet():
    greetings = ['Hola !', 'Hello :)', 'Sup '+("\U0001f60e"), 'Howdy '+ ("\U0001F607"), 'Greetings !', 'नमस्ते  '+("\U0001F64F") , 'وَعَلَيْكُمُ ٱلسَّلَامُ' , 'Ola !' , 'Allo !']
    return random.choice(greetings)