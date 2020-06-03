#lets get started
import requests;
#pretty print data now
from bs4 import BeautifulSoup
url="http://example.webscraping.com/places/default/view/Australia-14"
r=requests.get(url)
soup=BeautifulSoup(r.content,'html5lib')
#Lets Fetch Population
population=soup.find('tr',attrs={'id':'places_population__row'})
#print(str(population))
poulation_data=population.find('td',attrs={'class':'w2p_fw'})
#print("Population : "+str(poulation_data.text));
#Let's Try More

currency=soup.find('tr',attrs={'id':'places_currency_code__row'})
currency_data=currency.find('td',attrs={'class':'w2p_fw'})
#print("Currency : "+str(currency_data.text))

#Lets Try to Fetch all in Single Request
table=soup.find('table')
trs=table.findAll('tr')

for tr in trs:
	keys=tr.find('td',attrs={'class':'w2p_fl'})
	values=tr.find('td',attrs={'class':'w2p_fw'})
	print(str(keys.text)+" : "+str(values.text));