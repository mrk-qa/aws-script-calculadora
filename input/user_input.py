import os

def obter_escolha_usuario():
    print("Qual é o serviço? \n")
    print("1 - Instâncias do EC2")
    print("2 - Hosts dedicados do EC2")
    print("3 - Elastic Block Store (EBS) \n")

    escolha = input("Escolha uma opção: (1/2/3): ")

    print("\n ------------------------------------------------------------ \n")

    if escolha == "1":
        return "Instâncias do EC2"
    elif escolha == "2":
        return "Hosts dedicados do EC2"
    elif escolha == "3":
        return "Elastic Block Store (EBS)"
    else:
        print("Opção inválida \n")
        return obter_escolha_usuario()
    
print("\n ------------------------------------------------------------ \n")

service = obter_escolha_usuario()

sigla = input("Qual é a sigla? -->: ").upper()

def verificar_arquivo_excel(sigla):
    nome_arquivo = sigla + "_AWS.xlsx"
    
    if os.path.exists("siglas/excel/" + nome_arquivo):
        return True
    else:
        print (f"\n Arquivo {nome_arquivo} não encontrado \n")
        exit()
    
verificar_arquivo_excel(sigla)

print("\n ------------------------------------------------------------ \n")