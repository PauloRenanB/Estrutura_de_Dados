# 6. Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse
# número.

def calcFatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcFatorial(numero - 1)

numero = int(input("Digite um numero: "))

resultado = calcFatorial(numero)

print(resultado)