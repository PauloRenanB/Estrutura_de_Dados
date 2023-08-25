# 5. Faça um programa que leia uma lista de números e retorne a média dos números pares.

numPares = []

digite = int(input("Digite um valor: "))
for i in range(2, digite, 2):
    numPares.append(i)

soma = sum(numPares)
qntd = len(numPares)

media = soma / qntd

print(numPares)
print(media)
