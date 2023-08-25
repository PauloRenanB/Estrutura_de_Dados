# 2. Crie um programa que determine se um número inserido pelo usuário é par ou ímpar.

num = int(input("Digite um numero: "))

if num % 2 == 0:
    print(f"O número {num} é par!")
else:
    print(f"O número {num} é impar!")