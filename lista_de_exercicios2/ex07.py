# 7. Crie uma classe chamada “Carro” com atributos “marca”, “modelo” e “ano”. Implemente um método 
# chamado “detalhes” que retorna uma string com as informações do carro

class Carro:
    def detalhes(marca, modelo, ano):
        print(f"O carro é do modelo {modelo} da {marca}, ano {ano}")

carro = Carro()
carro = Carro.detalhes("Renault", "Kwid", 2020)