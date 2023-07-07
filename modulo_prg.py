# Este é um modulo(programa secundario do meu projeto)
#Iremos importar seus recursos e funções no programa main.py

# Uma função que calcula o maior valor de uma lista

def calculamaior(x,y,z):
    lista = [x,y,z]
    print(max(lista))

#  Criar uma soma

def soma(x,y):
    return x+y


# Contexto MAIN a função ou ação só será executada se for rodado diretamente no programa(script)

if __name__=='__main__':
    print(soma(2,3))
    print("Executei por aqui")