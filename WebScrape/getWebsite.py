from bs4 import BeautifulSoup
import urllib.request

weburl = input("Enter website url you wish to scrape here (ex: www.google.com): ")

countdot = weburl.count('.')

if (countdot == 2):

    urlpart_one = weburl[:4]

    if urlpart_one == "www.":
        try:
            addstr = "https://"
            webpage = urllib.request.urlopen(addstr+weburl).read()
            print ("Content Coming Soon :)")
        except Exception as e:
            print ("Unable to find website: " + str(e))
    else:
        print ("Incorrect url format" + countdot)
else:
    print ("Incorrect web url format")

