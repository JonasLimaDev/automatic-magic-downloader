from modulos import buscar_link, baixar, verificar_entrada,get_link_dados

if __name__ == "__main__":
    id_downloads = verificar_entrada(input("Digite o código do genoma: "))
    lista_downloads = []
    print("Opções:\n1 - Download do Genoma\n2 - Obter Link da Pasta")
    opcao = input("Digite a opção: ")

    for id in id_downloads:
        info=buscar_link(id)
        if info != None:
            lista_downloads.append(info)
    for dados in lista_downloads:
        if opcao == "1":
            baixar(dados)
        elif opcao == "2":
            get_link_dados(dados)
        else:
            print("Opção inválida tente novamente")

