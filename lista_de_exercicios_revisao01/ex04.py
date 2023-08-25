# 4. Crie um programa que leia uma lista de números e exiba o maior e o menor valor da lista.

lista = [2, 6, 4, 8, 1, 10, 14, 16, 40, 30, 21]
num_menor = 10000
num_maior = 0

for i in lista:
    if i > num_maior:
        num_maior = i

for n in lista:
    if n < num_menor:
        num_menor = n

print(num_maior)
print(num_menor)

