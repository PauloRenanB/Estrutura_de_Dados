# 4. Escreva um programa que recebe um número inteiro positivo e calcula a soma de seus dígitos.

numero = int(input("Digite um número inteiro: "))

numero_str = str(numero)
listaNum = []

for digito in numero_str:
    numeroint = int(digito)
    listaNum.append(numeroint)

print(listaNum)
soma = sum(listaNum)
print(soma)