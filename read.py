import json
import io
import requests
import datetime
from bs4 import BeautifulSoup
import urllib
def build():
    r = urllib.urlopen('https://www.livecoin.net/').read()
    time=datetime.datetime.now()
    soup = BeautifulSoup(r)

    letters=soup.find_all("li", class_="currency")
    timeOver=str(datetime.datetime.now()-time)


    n=1
    data=[]

    top={}
    datar={}

    with io.open('data.json', 'w', encoding='utf8') as outfile:
        top['name']=json.dumps("james",ensure_ascii=False)
        top['time']=timeOver
        top['provider']="livecoin"
        top['rawRequest']="r = urllib.urlopen('https://www.livecoin.net/')soup = BeautifulSoup(r)"
        top["currency"]=[]
        json_data=""
        for element in letters:
            name=element.span.get_text().strip()
            #datar= {"nameExchange" : element.span['data-currency'], "price": name}
            datar['nameExchange'] =json.dumps(element.span['data-currency'])
            datar['price'] = json.dumps(name)

        
            top['currency'].insert(0,[{'nameExchange' : element.span['data-currency'], 'Price' : name }])


        print "done"
        top=json.dumps(top)
        outfile.write((top.decode("utf8")))

