from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb://root:3215903287aA%40@142.93.198.98:27017/?authMechanism=DEFAULT")

# Select a database
db = client["scicollab"]

# Select a collection
collection = db["project_collection"]
newset=set()
all_documents = collection.find()
for i in all_documents:
	for x in i["keywords"]:
		newset.add(x)
print(newset)