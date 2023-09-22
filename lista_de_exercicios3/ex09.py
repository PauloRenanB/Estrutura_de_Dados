# 9. Crie uma calculadora que realiza operações de adição, subtração, multiplicação e divisão, com base
# na escolha do usuário.

def calculadora(num1,num2,escolha):
    if escolha == 1:
        somar = num1 + num2
        resultado = somar
    elif escolha == 2:
        subtrair = num1 - num2
        resultado = subtrair
    elif escolha == 3:
        dividir = num1 / num2
        resultado = dividir
    elif escolha == 4:
        multiplicar = num1 * num2
        resultado = multiplicar
    else:
        resultado = "Valor invalido!"

    return print(resultado)

escolha = int(input("Digite 1 para somar, 2 para subtrair, 3 para dividir e 4 para multiplicar: "))

num1 = int(input("Digite o valor 1: "))
num2 = int(input("Digite o valor 2: "))

calculadora(num1,num2,escolha)