# 3. Crie uma função que verifica se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente,
# desconsiderando espaços e pontuação).

palavra = input("Digite uma palavra para verificar se é um palindromo: ")

palavraInv = palavra[::-1]

def verificaPalindromo(palavra):
    if palavra == palavraInv:
        resultado = "A palavra é um palindromo!"
    else:
        resultado = "Não é um palindromo!"

    return print(resultado)

verificaPalindromo(palavra)

