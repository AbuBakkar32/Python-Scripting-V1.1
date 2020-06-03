
import requests;
from bs4 import BeautifulSoup

url="http://example.webscraping.com/places/default/view/Australia-14"
r=requests.get(url)
soup=BeautifulSoup(r.content,'html5lib')
population=soup.find('tr',attrs={'id':'places_population__row'})

#print(str(population))
poulation_data=population.find('td',attrs={'class':'w2p_fw'})
#print("Population : "+str(poulation_data.text));

currency_tr=soup.find('tr',attrs={'id':'places_currency_code__row'})
currency_data=currency_tr.find('td',attrs={'class':'w2p_fw'})
#print("Currency : "+str(currency_data.text))

#Lets Try to Fetch all in Single Request
findTable=soup.find('table')
Findtrs=findTable.findAll('tr')

for findtr in Findtrs:
	keys=findtr.find('td',attrs={'class':'w2p_fl'})
	values=findtr.find('td',attrs={'class':'w2p_fw'})
	print(str(keys.text)+" : "+str(values.text));
