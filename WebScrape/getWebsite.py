from bs4 import BeautifulSoup
import urllib.request
import pandas as pandas
import time
from openpyxl import load_workbook
import re


weburl = 'https://coinmarketcap.com/'

try:
    webpage = urllib.request.urlopen(weburl).read()
    soup = BeautifulSoup(webpage, 'lxml')
    get_currency_name = soup.find_all('a', 'currency-name-container')
    get_market_cap = soup.find_all('td', 'market-cap')
    get_price = soup.find_all('a', 'price')
    get_volume = soup.find_all('a', 'volume')
    get_coin_supply = soup.find_all("span", attrs={"data-supply-container": re.compile(r".*")})
  
    count = 0

    rank = []
    cryptoName = []
    cryptoMarketcap = []
    cryptoPrice = []
    cryptoVolume = []
    cryptoSupply = []


    while count < 100:
        rank.append(count+1)
        cryptoName.append(get_currency_name[count].get_text())
        cryptoMarketcap.append(get_market_cap[count].get_text())
        cryptoPrice.append(get_price[count].get_text())
        cryptoVolume.append(get_volume[count].get_text())
        cryptoSupply.append(get_coin_supply[count].get_text())
        count = count + 1

    currentDay = time.strftime("%m-%d-%Y")
    currentTime = time.strftime("%I-%M-%S %p")

    loadFile = load_workbook('coininfo.xlsx')
    writer = pandas.ExcelWriter('coininfo.xlsx', engine='openpyxl')
    writer.book = loadFile

    addInfo = pandas.DataFrame({'Rank #:': rank, 'Crypto Name:': cryptoName, 'Market Cap:': cryptoMarketcap, 'Price:': cryptoPrice, 'Volume:': cryptoVolume, 'Coin Supply:': cryptoSupply}, columns=['Rank #:', 'Crypto Name:', 'Market Cap:', 'Price:', 'Volume:', 'Coin Supply:'])
    addInfo.to_excel(writer, sheet_name='Dash_'+currentDay+'_'+ currentTime, index=False)

    writer.save()
    writer.close()
except Exception as e:
    print ("Error: " + str(e))


