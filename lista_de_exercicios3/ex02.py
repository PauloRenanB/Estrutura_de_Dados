# 2. Escreva uma função que calcula o fatorial de um número inteiro positivo fornecido pelo usuário.

numero = int(input("Fatorial de: "))

def verificarFatorial(numero):
    resultado = 1
    for n in range(1, numero + 1):
        resultado *= n
    return print(resultado)

verificarFatorial(numero)


