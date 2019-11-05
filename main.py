from bs4 import BeautifulSoup
import urllib3
import requests
from ftplib import FTP
from modulos import buscar_link, baixar

url=buscar_link(input("Digite o código do genoma: "))
baixar(url)
