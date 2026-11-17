# Arquivo: 08_caixa_eletronico.py

# Desenvolva um caixa eletrônico simples com saldo inicial de R$ 500.00.

# O programa deverá apresentar o seguinte menu:

# === CAIXA ELETRÔNICO ===
# 1 - Consultar saldo
# 2 - Depositar dinheiro
# 3 - Sacar dinheiro
# 0 - Sair
# Regras:

# O menu deverá continuar funcionando até que o usuário escolha sair.
# Depósitos e saques devem possuir valores maiores que zero.
# Não será permitido sacar mais dinheiro do que existe na conta.
# O saldo deverá ser atualizado após depósitos e saques válidos.
# Opções inválidas devem apresentar uma mensagem de erro.
# Desafio adicional: conte quantos depósitos e saques foram realizados durante a execução.




saldo = 500.00

while  True:

    print("1 - qual o saldo")
    print("2 - qual valor foi depositado")
    print("3 - qual valor do saque")
    print("0 - sair")

    opcao = int(input("escolha uma opcao= "))

    if opcao == 1:
        print("Seu saldo é de R$", saldo)
    
    elif opcao == 2:    
        deposito = float(input("digite um valor: R$ "))
        saldo += deposito
        print("Valor depositado com sucesso") 

    elif opcao == 3:
        saque = float(input("digite um valor: R$ "))
        saldo-= saque
        print("valor sacado com sucesso")
    elif opcao == 0:
        print("saindo")
        break 
    else:
        print("opcao invalida")