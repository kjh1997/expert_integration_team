from json.tool import main
import pymongo
import time, json

client = pymongo.MongoClient('203.255.92.141:27017', connect=False)
SCI = client['SCIENCEON']
KCI = client['KCI']
sciData = SCI['Rawdata'].find({"keyId":711})
main_data = {}
for doc in sciData:
    p_id = str(doc['_id'])
    a_id = doc['author_id'].split(";")
    a_name = doc['author']

    main_data[p_id] = {}
    main_data[p_id]["author"] = []
    main_data[p_id]["title"] = doc["title"]
    main_data[p_id]["abstract"] = doc['abstract']
    main_data[p_id]["keyword"] = doc['paper_keyword']
    main_data[p_id]["venue"] = doc['journal']
    main_data[p_id]["year"] = doc['issue_year']
    for i in a_id:
        a_data = {}
        a_data['org'] = SCI['Author'].find_one({"_id":i})['inst']
        a_data['name'] = SCI['Author'].find_one({"_id":i})['name']
        a_data['id'] = SCI['Author'].find_one({"_id":i})['_id']
        main_data[p_id]["author"].append(a_data)
print(main_data)
with open("pubs_raw.json",'w', encoding='UTF-8-SIG')as file:
    file.write(json.dumps(main_data, default=str, indent=2, ensure_ascii=False))
    





