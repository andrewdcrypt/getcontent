from bs4 import BeautifulSoup
import urllib.request
import pandas as pandas

weburl = 'https://coinmarketcap.com/'

try:
    webpage = urllib.request.urlopen(weburl).read()
    soup = BeautifulSoup(webpage, 'lxml')
    get_currency_name = soup.find_all('a', 'currency-name-container')

    count = 0

    rank = []
    cryptoName = []

    while count < 100:
        rank.append(count+1)
        cryptoName.append(get_currency_name[count].get_text())
        print ('Rank#: '+ str(count+1) + ' Name:' + str(get_currency_name[count].get_text()))
        count = count + 1

    addInfo = pandas.DataFrame({'Rank #:': rank, 'Crypto Name:': cryptoName}, columns=['Rank #:', 'Crypto Name:'])
    addInfo.to_excel('coininfo.xlsx', sheet_name='Dash', index=False)

except Exception as e:
    print ("Error: " + str(e))


