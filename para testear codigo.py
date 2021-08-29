import random

lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [7,8,9]
lista = [lista1,lista2,lista3]
respuestas = []
cuenta = 0
while cuenta < 3:
    x = random.choice(lista[0])
    respuestas.append(x)
    lista[0].remove(x)

    cuenta += 1



xd = 4
if a >xd