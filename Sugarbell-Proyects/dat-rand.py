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


'''
Frase1,Frase2,Frase3,Frase4,Frase5,Frase6,Frase7,Frase8,Frase9,Frase10,Frase11,Frase12,Frase13,Frase14,Frase15,Frase16,Frase17,Frase18,Frase19,Frase20
'''
