from bs4 import BeautifulSoup
import urllib.request

weburl = 'https://coinmarketcap.com/'

try:
    webpage = urllib.request.urlopen(weburl).read()
    soup = BeautifulSoup(webpage, 'lxml')
    get_currency_name = soup.find_all('a', 'currency-name-container')

    count = 0

    while count < 100:
        print ('Rank#: '+ str(count+1) + ' Name:' + str(get_currency_name[count].get_text()))
        count = count + 1

except Exception as e:
    print ("Error: " + str(e))


