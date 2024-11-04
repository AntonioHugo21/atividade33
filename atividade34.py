lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,]

print(f'O intervalo entre 1 e 9 é {lista[1:10]}!')
print(f'O intervalo entre 8 e 13 é {lista[8:14]}')
pares = []
impares = []
multiplos_de_3 = []
multiplos_de_4 = []
divisao_entre_intervalos = sum(lista[10:16]) / sum(lista[3:10])
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

for numero in range (0, (5 * 3) + 1, 3):
    multiplos_de_3.append(numero)
for numero in range(0, (3 * 4) + 1, 4 ):
    multiplos_de_4.append(numero)
    
print(f'Os números pares da lista são {pares}')
print(f'Os números ímpares da lista são {impares}')
print(f'Os números multiplos de 2 são {pares}')
print(f'Os números multiplos de 3 são {multiplos_de_3}')
print(f'Os números multiplos de 4 são {multiplos_de_4}')
lista.sort(reverse = True)
print(f'O reverso da lista é {lista}')
lista.sort()

print('A divisão entre os intervalos de 10 e 15 e 3 e 9 é {:.2f}!'.format(divisao_entre_intervalos))
