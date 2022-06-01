from bs4 import BeautifulSoup
import requests
import os
import wget


def verificar_entrada(entrada):
	lista_entrdas = []
	if ',' in entrada:
		lista_entrdas = entrada.split(',')
	else:
		lista_entrdas=[entrada]
	print(lista_entrdas)
	return(lista_entrdas)


def buscar_link(id):
	print("buscando link")
	dados = {}
	html= requests.get("https://www.ncbi.nlm.nih.gov/genome/"+str(id))
	if html.status_code == 200:
		bs = BeautifulSoup(html.text,'html.parser')
		resultados= bs.find_all('span')		
		for r in resultados:
			if "Download sequences in FASTA format for genome" in r.get_text() :
				texto=r.find('a')
				dados['link'] = texto['href']
		resultados_2  = bs.find_all('span',{"class": "GenomeTitle"})
		organismo = resultados_2[0].get_text()
		organismo = organismo.split("(")[0][:-1]
		dados['nome'] = organismo
		print(f"link para {organismo} \033[92mEncontrado\033[0m")
		return dados
	elif html.status_code == 404:
		print(f"Nada Encontrado para o ID {id}")
		return None
	else:
		print(f"Erro Inesperado para o ID {id}")
		return None


def baixar(dados):
	if dados != None:
		local_download =  f"./downloads/{dados['nome']}"
		if not os.path.exists(local_download):
			os.makedirs(local_download)
		print(f"Baixando: {dados['nome']}")
		wget.download(dados['link'],local_download)
		print(f"\nFinalizado o download do Genoma: {dados['nome']}")
	else:
		pass

if __name__ == "__main__":
	pass

