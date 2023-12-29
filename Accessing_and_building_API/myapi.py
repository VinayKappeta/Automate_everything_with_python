from flask import Flask, jsonify
from bs4 import BeautifulSoup as bs
import requests

def get_currency(in_currency,out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    print(url)
    content = requests.get(url).text
    #print(content)
    soup = bs(content,'html.parser')
    x = soup.find("span", class_ = "ccOutputRslt").get_text()
    rate = (x.split(" ")[0])
    return rate

app = Flask(__name__)

@app.route('/')

def home():
    return '<h1> Currency Rate API </h1> <p> Example URL: /api/v1/usd-eur</p>'

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur,out_cur):
    rate = get_currency(in_cur, out_cur) 
    result_dict = {'input_currency':in_cur,'output_currency':out_cur,"rate":rate}
    return jsonify(result_dict)
app.run(host = '0.0.0.0')