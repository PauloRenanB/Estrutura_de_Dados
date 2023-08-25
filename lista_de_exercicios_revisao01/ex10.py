# 10. Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o computador. O
# programa deve solicitar a escolha do usuário e, em seguida, escolher aleatoriamente a escolha do
# computador e determinar o vencedor.

from random import randint
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0,2)
escolhaComputador = itens[computador]

print("Suas opções: 0 > Pedra, 1 > Papel, 2 > Tesoura")

opcao = int(input("Digite o valor de sua opção: "))
escolha = itens[opcao]


if escolhaComputador == escolha:
    print("Empate!")
elif escolhaComputador == "Pedra" and escolha == "Papel":
    print("Voce ganhou!")
elif escolhaComputador == "Pedra" and escolha == "Tesoura":
    print("Voce perdeu")
elif escolhaComputador == "Papel" and escolha == "Pedra":
    print("Voce perdeu")
elif escolhaComputador == "Papel" and escolha == "Tesoura":
    print("Voce ganhou")
elif escolhaComputador == "Tesoura" and escolha == "Pedra":
    print("Voce ganhou")
elif escolhaComputador == "Tesoura" and escolha == "Papel":
    print("Voce perdeu!")

print(f"Voce escolheu {escolha}")
print(f"O adversario escolheu {escolhaComputador}")

