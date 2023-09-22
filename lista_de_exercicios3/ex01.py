# 1. Escreva um programa que recebe cinco notas de um aluno e calcula a média. Em seguida, exiba se o
# aluno foi aprovado (média maior ou igual a 7) ou reprovado (média menor que 7).

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))
nota5 = int(input("Digite a quinta nota: "))

soma = nota1 + nota2 + nota3 + nota4 + nota5
media = soma / 5

if media >= 7:
    print(f"Aprovado. Media: {media:.2f}")
else:
    print(f"Reprovado. Media: {media:.2f}")