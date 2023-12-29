import requests
from datetime import datetime
import time
'''https://query1.finance.yahoo.com/v7/finance/download/ADANIPOWER.NS?period1=1672287875&period2=1703823875&interval=1d&events=history&includeAdjustedClose=true
https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=1672269908&period2=1703805908&interval=1d&events=history&includeAdjustedClose=true
'''
ticker = input("Enter the company: ")
from_date = input("Enter the start date in yyyy/mm/dd format: ")
to_date = input("Enter the end date in yyyy/mm/dd format:")

f_d = datetime.strptime(from_date,'%Y/%m/%d')
t_d = datetime.strptime(to_date,'%Y/%m/%d')

from_epoch = int(time.mktime(f_d.timetuple()))
to_epoch = int(time.mktime(t_d.timetuple()))

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"
print(url)
headers = {"User-Agent":"Mozilla/5.0(X11; Linux x86_64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

content = requests.get(url,headers = headers).content
print(content)

with open(f'//config//workspace//Webscrapping//{ticker}_data.csv','wb') as file:
    file.write(content)

