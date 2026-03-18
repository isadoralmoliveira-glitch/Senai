estoque = []


print("------------------------------------".center(100))
print("Bem Vindo!".center(100))
print("------------------------------------".center(100))

nome = input("Digite seu nome: ")

print("------------------------------------".center(100))
print(f"Bem vindo, {nome}".center(100))
print("------------------------------------\n".center(100))

#menu#
while True:
    ##while é um tipo de tag usada para repetição, e só para quando der o comando para parar
    print("O que desejas?\n")
    print("1- Adicionar uma entrada ao estoque")
    print("2- Registrar uma saída de produtos no estoque")
    print("3- Ver estoque")
    print("Sair\n")
    opcao = float(input("Selecione uma opção: "))

#entrada#
    
    if opcao == 1:
        while True:
            print("------------------------------------".center(100))
            print("ENTRADA".center(100))
            print("------------------------------------\n".center(100))
            produto = input("Digite o nome do produto: ")
            input("Digite a quantidade de produtos: ")
            estoque.append(produto)
            print(f"Você adicionou {produto} ao estoque.")
            print("Deseja voltar ao menu?\n")
            print("1- Sim")
            print("2- Não")
            voltar = int(input("Deseja voltar ao menu: \n"))
            if voltar == 1:
                 print("Voltando ao menu...\n")
                 break
            ##break serve para interromper a ação do while, interrompendo a repetição
            else:
                 None
            
                  
#saída#

    
    if opcao == 2:
            while True:
                print("------------------------------------".center(100))
                print("SAÍDA".center(100))
                print("------------------------------------\n".center(100))
                saida = input("Digite o nome do produto: ")
                input("Digite a quantidade de produtos: ")
                print(f"Você removeu {produto} do estoque.") 
                print("Deseja repetir o processo?\n")
                print("1- Sim")
                print("2- Não")
                repetir = float(input("Deseja repetir o processo?: "))
                if repetir == 1:
                    None
                else:
                    print("Voltando ao menu...")
                    break    

#ver estoque#

    if opcao == 3:
        print(estoque)
        print("Deseja sair?\n")
        print("1- Sim")
        print("2- Não")
        bye = float(input("Deseja sair?: "))
        if bye == 1:
            break
        else:
            None
         

#sair#

    if opcao == 4:
        print("Até a proxima!")
        break