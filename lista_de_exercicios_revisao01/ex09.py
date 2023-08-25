# 9. Escreva um programa que leia uma lista de nomes e retorne uma nova lista com apenas os nomes que
# começam com a letra 'A'.

nomes = ["Amanda", "Bruna", "Pedro", "Alberto", "Alice", "João", "Marcia", "Acacio", "Amarildo"]
nomesA = []
nomesSemA = []

for i in nomes:
    if i[0] == "A":
        nomesA.append(i)
    else:
        nomesSemA.append(i)


print(nomesA)
print(nomesSemA)
