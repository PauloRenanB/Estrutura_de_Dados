# 7. Crie uma função que calcula o índice de massa corporal (IMC) de uma pessoa com base em sua altura
# e peso.

def calcIMC(peso,altura):
    resultado = peso / (altura*altura)
    return print(resultado)

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

calcIMC(peso,altura)