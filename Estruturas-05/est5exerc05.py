# Arquivo: 05_media_turma.py

# Solicite quantos alunos existem em uma turma.

# Em seguida, leia a nota de cada aluno e calcule a média geral.

# # A quantidade de alunos deve ser maior que zero.



qtd = int(input("diga quantos alunos tem a turma: ")) 
contador = 1
soma = 0

while contador <= qtd:
    nota = float(input(f"Digite a nota do {contador}º aluno: "))
    soma += nota
    contador += 1

media = soma/qtd

print(f"A média da turma ficou em: {media}")

# float= ("aluno/nota")==("media")

# print ("media da turma")





    