# 8. Faça um programa que determine se um número é primo ou não.

def verificaPrimo(numero):
    if numero < 2:
        return False
    for i in range (2, int(numero ** 0.5) +1):
        if numero % i == 0:
            return False
    return True

num = int(input("Digite um valor: "))

if verificaPrimo(num):
    print(f"{num} é primo!")
else:
    print(f"{num} não é primo!")