from modulos import buscar_link, baixar, verificar_entrada

if __name__ == "__main__":
    id_downloads = verificar_entrada(input("Digite o código do genoma: "))
    lista_downloads = []
    for id in id_downloads:
        info=buscar_link(id)
        if info != None:
            lista_downloads.append(info)
    for dados in lista_downloads:
        baixar(dados)
