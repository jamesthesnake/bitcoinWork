import math
import sys
import logging
import pprint
import json
import pymysql
def store():
    db = pymysql.connect(host='165.227.79.78',user='jake',passwd='HiMommy12',db="JSONDB")
    file="data.json"

    with open(file) as data_file:    
    
        json_obj=json.load(data_file)

    name= json_obj['currency'][1][0]['nameExchange']
    dbz=db.cursor()

    for j in range(0,len(json_obj['currency'])):
        numPrice=  json_obj['currency'][j][0]['Price']
        name= json_obj['currency'][j][0]['nameExchange']


        dbz.execute("UPDATE JSONBITCOIN SET Price =%s Where Currency='"+ name+"'",[str(numPrice)])
#path="http://ec2-34-211-157-17.us-west-2.compute.amazeonaws.com/phpmyadmin"
