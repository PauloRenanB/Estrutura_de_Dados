# 5. Crie uma classe chamada “Pessoa” com atributos “nome” e “idade”. Implemente um método 
# chamado “falar” que imprime uma mensagem com o nome da pessoa

class Pessoa:
    def falar(nome, idade):
        print(f"Olá, {nome}. Você tem {idade} mesmo??")

falar = Pessoa()
falar = Pessoa.falar("Paulo Renan", 20)
    