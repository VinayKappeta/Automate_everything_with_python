from bs4 import BeautifulSoup as bs
import requests

def get_currency(in_currency,out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    print(url)
    content = requests.get(url).text
    #print(content)
    soup = bs(content,'html.parser')
    x = soup.find("span", class_ = "ccOutputRslt").get_text()
    print(x.split(" ")[0])
get_currency('USD','EUR')