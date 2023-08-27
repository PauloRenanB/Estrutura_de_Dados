# 8. Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado 
# “calcular_media” que retorna a média das notas do aluno

class Aluno:
    def calcular_media(self, nome, nota1, nota2, nota3):
        media = (nota1 + nota2 + nota3) / 3
        print(f"Media: {media}. Aluno: {nome}")
        return media
    
aluno1 = Aluno()
aluno1.calcular_media("Paulo Renan", 10, 7, 7)