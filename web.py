from bs4 import BeautifulSoup #type:ignore
import requests #type:ignore
url ="https://zetrance.com/"
response = requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
print(soup)