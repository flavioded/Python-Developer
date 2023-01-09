menu = """

###MENU###

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""


saldo = 0
limite = 500
extrato = ""
numero_saques = 0 
LIMITES_SAQUES = 3
total = 0

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Digite o valor que deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito no valor de R$ {valor:.2f}\n"
            total += valor
            
        else:
            print("Operação falhou. O valor informado é inválido")

    elif opcao == "s":
        
        if numero_saques < LIMITES_SAQUES:
            
        
            valor = float(input("Digite o valor que deseja sacar: "))
        
            if valor <= saldo:
                print(f"Realizando o saque de R$ {valor:.2f}\n")
                saldo -= valor
                extrato += f"Saque no valor de R$ {valor:.2f}\n"
                numero_saques += 1
                total -= valor
            
            elif valor > saldo:
                print("Saldo insuficiente")
        
        else:
            print("Erro na operação! Número de saques excedido\n")
            
        
        
        
    elif opcao == "e":
        print("====== EXTRATO ======\n")
        print(extrato)
        if not extrato:
            print("Não houve movimentações na conta")
        print (f"O saldo total é de R${total:.2f}\n")
        print("=====================")

    
    elif opcao == "q":
        break
    
    else:
        print("Opção inválida")



