# 7. Crie um programa que imprima a sequência de Fibonacci até um valor inserido pelo usuário.

def fibonacci_sequence(n):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= n:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence

valor = int(input("Insira um valor limite para a sequência de Fibonacci: "))

fib_sequence = fibonacci_sequence(valor)
print("Sequência de Fibonacci até", valor, ":", fib_sequence)