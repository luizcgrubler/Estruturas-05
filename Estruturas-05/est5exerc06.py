# Arquivo: 06_validacao_nota.py

# Solicite uma nota entre 0 e 10.

# Enquanto o usuário informar um valor fora desse intervalo, apresente Nota inválida e solicite novamente.

# Quando uma nota válida for informada, mostre Nota registrada com sucesso!.



nota = float(input("digite uma nota entre zero e dez"))

while nota < 0 or nota > 10:
    nota = float(input("nota invalida. digite uma nota entre zero e dez:"))

print ("nota registrada com sucesso")









