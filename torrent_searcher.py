import os
def install():
	try:
		import requests
	except:
		os.system('pip install requests')
	try:
		from bs4 import BeautifulSoup
	except:
		os.system('pip install bs4')
	try:
		import lxml
	except:
		os.system('pip install lxml')
install()

import requests
from bs4 import BeautifulSoup
import lxml

path=os.getcwd()

def piratesbay(query):
	query = query.replace(' ','%20')
	proxies_site_list = 'https://piratebayproxy.info/'
	source = requests.get(proxies_site_list).text
	soup = BeautifulSoup(source,'lxml')
	proxies_list = []

	for line in soup.find_all('td',class_='site'):
		site = 'https:\\'+line.a.text
		proxies_list.append(site)
	current_proxy = proxies_list[0]
	api_endpoint = f'/search/{query}/1/99/0'
	command = f'start "" "{current_proxy+api_endpoint}"'
	print(command)
	os.system(command)

def limetorrents(query):
	query = query.replace(' ','-')
	proxies_list = ['https://www.limetorrents.info/','https://limetorrents.co/']
	current_proxy = proxies_list[0]
	api_endpoint = f'search/all/{query}/'
	
	command = f'start "" "{current_proxy+api_endpoint}"'
	print(command)
	os.system(command)

def torrent_1337x(query):
	query = query.replace(' ','+')
	proxies_list = ['https://1337x.to/','https://1337xto.to/','https://1337x.gd/']
	current_proxy = proxies_list[0]
	api_endpoint = f'search/{query}/1/'
	
	command = f'start "" "{current_proxy+api_endpoint}"'
	print(command)
	os.system(command)

def rarbg(query):
	query = query.replace(' ','+')
	proxies_list = ['https://rarbgprx.org/']
	current_proxy = proxies_list[0]
	api_endpoint = f'torrents.php?search={query}'
	
	command = f'start "" "{current_proxy+api_endpoint}"'
	print(command)
	os.system(command)

def kickass_torrents(query):
	query = query.replace(' ','+')
	proxies_list = ['https://kickasstorrentcr.top/'] 
	current_proxy = proxies_list[0]
	api_endpoint = f'search.php?q={query}&cat=0'

	command = f'start "" "{current_proxy+api_endpoint}"'
	print(command)
	os.system(command)

while True:
	query = input("Enter torrent to be searched: ")
	piratesbay(query)
	limetorrents(query)
	kickass_torrents(query)
	torrent_1337x(query)
	rarbg(query)
	print("\n[Finished]\n")
