from json.tool import main
import pymongo
import time
import json, datetime
keyid = 711
client = pymongo.MongoClient('203.255.92.141:27017', connect=False)
SCI = client['SCIENCEON']
KCI = client['KCI']
a_paperdb = SCI['AuthorPapers']
sciData = SCI['Rawdata'].find({"keyId":keyid})
main_data = {}

for doc in sciData:
    a_name = doc['author'].split(";")
    a_id = doc['author_id'].split(";")
    for i in range(len(a_name)-1):
        if a_name[i] in main_data:
            
            main_data[a_name[i]][a_id[i]] = a_paperdb.find_one({"A_ID": a_id[i], "keyId":keyid})["papers"]
        else: 
            main_data[a_name[i]] = {}
            main_data[a_name[i]][a_id[i]] = a_paperdb.find_one({"A_ID": a_id[i], "keyId":keyid})["papers"]
print(main_data)
with open("name_to_pubs.json",'w', encoding='UTF-8')as file:
    file.write(json.dumps(main_data, default=str, indent=2, ensure_ascii=False))
    
