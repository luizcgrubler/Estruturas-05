# # Arquivo: 07_menu.py

# # Crie um menu com as seguintes opções:

# # === MENU ===
# # 1 - Somar dois números
# # 2 - Verificar maioridade
# # 0 - Sair
# # O menu deverá continuar aparecendo até o usuário escolher a opção 0.

# # Utilize while True, condicionais e break.





while True:

    print ("\n=== menu ===")
    print ("1 - somar os dois numeros")
    print ("2 - verificar maioridade")
    print ("0 - sair")


    opcao = input("escolha uma opcao=")

    if opcao == "1":
        
        num1 = int(input("digte um número: "))
        num2 = int(input("Digite outro número: "))
        print("\nA soma dos números é:", num1 + num2)


    elif opcao == "2":

        numero = int (input("digite um numero: "))
        numero2 = int(input("Digite outro número: "))

        if numero > numero2:
            print(f"\nO número {numero} é o maior!")
        elif numero2 > numero:
            print(f"\nO número {numero2} é o maior!")
        else:
            print("\nAmbos são iguais!")

    elif opcao == "0":
        print ("\nencerrado...")
        break

    else:
        print ("opcao invalida")









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

# Resumo do tópico
# Conceito	Finalidade
# while	Repete instruções enquanto uma condição for verdadeira
# Contador	Conta quantas vezes algo aconteceu
# Acumulador	Guarda valores que são somados ou atualizados
# +=	Incrementa uma variável
# -=	Decrementa uma variável
# while True	Cria uma repetição contínua
# break	Interrompe uma repetição
# Próximo tópico: estrutura de repetição for e utilização de range().





# contador = 1
# soma = 0

# while contador >= 3