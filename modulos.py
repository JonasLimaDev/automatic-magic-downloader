from bs4 import BeautifulSoup
import urllib3
import requests
from ftplib import FTP

def buscar_link(id):
	print("buscando link\n")
	#http = urllib3.PoolManager()
	#html=http.request('GET',"https://www.ncbi.nlm.nih.gov/genome/"+str(id))
	html= requests.get("https://www.ncbi.nlm.nih.gov/genome/"+str(id))
	bs = BeautifulSoup(html.text,'html.parser')
	resultados= bs.find_all('span')
	for r in resultados:
		
		if "Download sequences in FASTA format for genome" in r.get_text() :
			texto=r.find('a')
			link=texto['href']
	print("Link encontrado")
	return link


def baixar(link):
	arquivo=link.split('/')[-1]
	#print(arquivo)
	site=link.rsplit(arquivo, 1)[0]
	site=site.rsplit("ftp://ftp.ncbi.nlm.nih.gov/", 1)[1]
	#print(site)
	ftp = FTP('ftp.ncbi.nlm.nih.gov')
	ftp.login()
	ftp.cwd(site)
	files = ftp.nlst()
	#print(files)
	for file in files:
		if file == arquivo:
			print("Baixando... " + file)
			ftp.retrbinary("RETR " + file ,open("./" + file, 'wb').write)
			print("\nFinalizado transferência do arquivo: " + file)
	ftp.close()

