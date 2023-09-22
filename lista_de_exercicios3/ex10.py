# 10. Escreva uma função que gera a sequência de Fibonacci até um determinado número de termos
# especificado pelo usuário.

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

num_termos = int(input("Digite o número de termos da sequência de Fibonacci desejados: "))

resultado = fibonacci(num_termos)

print(resultado)