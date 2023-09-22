# 5. Crie uma função que verifica se um número é primo ou não.

num = int(input("Digite um número: "))

def verificarPrimo(num):
    if num % 2 == 0:
        resultado = "Não é primo"
    else:
        resultado = "É primo"

    return print(resultado)

verificarPrimo(num)
