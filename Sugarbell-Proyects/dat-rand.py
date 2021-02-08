import random
from clipboard import copy
inp = input('Ingresa Lista de Frases: ')
ins = inp.split(',')
it = ins[0:]
print (it)
rait = random.choices(it)
rastr = ' '.join(rait)

copy(rastr)
print(rastr)


