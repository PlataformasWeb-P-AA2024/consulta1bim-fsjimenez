import csv
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['tennis']  
collection = db['matches']  

with open('atp_tennis.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        collection.insert_one(row)

print("Datos insertados en la base de datos.")

matches = collection.find({}, {'_id': 0})  
print("Consulta en MongoDB:")
for match in matches:
    print(match)
