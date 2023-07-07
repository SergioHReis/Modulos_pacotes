# O main.py é o arquivo principal do meu projeto
# onde iremos executa-lo direatamente e iremos
#importar funções e recursos de outros modulos.

import modulo_prg

# Importando de forma restritiva os recursos de um pacote 

from pacote.prog1 import var1,listacarros,calculopercentual
from pacote.prog2 import listapares


modulo_prg.calculamaior(1,4,100)

print(modulo_prg.soma(5,4))

print(var1)

print(calculopercentual(1000,10))
print(listacarros)

listapares(41)


