# 6. Escreva um programa que recebe uma string e conta a quantidade de vogais (a, e, i, o, u) presentes
# nela.

palavra = input("Digite uma palavra: ")

letras = []
vogais = []

for i in palavra:
    letras.append(i)

for l in letras:
    if l == "a" or l =="e" or l == "i" or l == "o" or l == "u":
        vogais.append(l)

print(vogais)
quantidadeVogais = len(vogais)

print(quantidadeVogais)
