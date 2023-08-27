# 6. Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. Implemente um 
# método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade).

class Produto:
    def calcular_total(nome, preco, quantidade):
        valor_total = preco * quantidade
        print(f"Você compro {nome}. Por R${preco} e {quantidade} unidades. Pagou no total {valor_total}")
        return valor_total
    
produto = Produto()
produto = Produto.calcular_total("Laranja", 0.50, 30)
    

