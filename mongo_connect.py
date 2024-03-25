from pymongo import MongoClient

#create the connection url
connecturl = "mongodb://127.0.0.1:27017/"

# connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)

# select the 'training' database

db = connection.training

# select the 'mongodb_glossary' collection

collection = db.languages

# create documents

doc1 = {"database1":"a database contains collections"}
doc2 = {"collection":"a collection stores the documents"}
doc3 = {"document":"a document contains the data in the form or key value pairs."}

# insert documents
print("Inserting documents into collection.")

collection.insert_one(doc1)
collection.insert_one(doc2)
collection.insert_one(doc3)

# query for all documents in 'training' database and 'python' collection

docs = collection.find()

print("Printing the documents in the collection.")

for document in docs:
    print(document)

# close the server connecton
print("Closing the connection.")
connection.close()