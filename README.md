## Instalacao Mongodb no ubuntu

- Baixe o Mongodb community na extensao .deb em https://www.mongodb.com/try/download/community 

Para instalar:
```
sudo dpkg -i mongodb-org-server_7.0.5_amd64.deb # (versao 7.0.5) 
```

Verifique se foi inicializado:
```
sudo systemctl status mongod
```

Caso ele nao esteja iniciado:
```
sudo systemctl start mongod
```
### Instalacao Mongodb Shell no ubuntu

- Baixe o Mongodb Shell em https://www.mongodb.com/try/download/shell. Para instalar:
```
sudo dpkg -i mongodb-mongosh_2.1.4_amd64.deb
```

Execute o shell do mongodb com o comando mongosh.

- Voce tambem pode instalar uma interface grafica, o mongo db compass, obtenha o .deb em  https://www.mongodb.com/try/download/compass

```
sudo dpkg -i mongodb-compass_1.42.1_amd64.deb
```

Para inicializar o terminal do mongo
```
mongosh
```

## Comandos básicos

Verifica versão:
- db.version() 

Mostra os databases existentes:
- show dbs

Cria o database e muda para ele:
- use training

Cria uma coleçao no database selecionado:
- db.createCollection("mycollection")

Mostra as coleçoes no database:
- show collections

Para contar os numero de documentos:
- db.mycollection.countDocuments()

## Operações CRUD no Mongodb

Para inserir um documento:
```
db.mycollection.insertOne({"firstName":"John", "lastName": "Doe", "email":"john.do@mail.com", "studentId":20217484})
```

Para inserir uma lista de documentos:
```
students_list = [{"firstName":"Sara", "lastName": "Connor", "email":"sara.connor@mail.com", "studentId":20217485}, {"firstName":"Alex", "lastName": "Doe", "email":"alex.doe@mail.com", "studentId":20217486}]

db.mycollection.insertMany(students_list)
```
    
Para listar os documentos:
```
db.mycollection.find()
```

Para listar apenas um documento que satisfaz a condição:
```
db.mycollection.findOne({"email":"sara@gmail.com"})
```

Para listar todos os documento que satisfaz a condição:
```
db.mycollection.find({"email":"sara@gmail.com"})
```
Para restringir campos, podemos exemplo abaixo  fazer como nos exemplos abaixo que mostram apenas o campo name e mostram todos os campos exceto o campo name respectivamente
```
db.languanges.find({},{"name":1})
db.languanges.find({},{"name":0})
```

Por exemplo, para mostrar o campo name apenas para os itens que satisfazem type = object oriented
```
db.languagens.find({"type":"object oriented"},{"name":1})
```

Para atualizar documentos, inserindo os campos onlineOnly e email em documentos que 
satisfaçam a condição lastName = Doe.
```
changes = {$set: {"onlineOnly":true,"email":"john@campus.edu"}}
db.mycollection.updateOne({"lastName":"Doe"}, changes)
```
Para inserir o campo onlineOnly em todos os documentos da coleção:
```
db.mycollection.updateMany({},{"$set": {"onlineOnly": true}})
```

Apagar um item que satisfaz a condição:
```
db.languanges.deleteOne({"name":"scala"})
```

Apaga todos os itens que satisfaz a condição
```
db.languanges.deleteMany({"name":"scala"})
```

## Index 

Para otimizar as queries podemos criar indices no campos mais buscados (isso tem um custo relativo a memória).

No seguinte exemplo vamos popular uma coleção 
```
use training
for (i=1;i<=200000;i++){print(i);db.bigdata.insert({"account_no":i,"balance":Math.round(Math.random()*1000000)})}
```

```
db.bigdata.countDocuments()
```
E realizar uma busca, cronometrando quanto tempo demora para retornar o resultado
```
db.bigdata.find({"account_no":58982}).explain("executionStats").executionStats.executionTimeMillis
```
Crie um index
```
db.bigdata.createIndex({"account_no":1})
db.bigdata.getIndexes()
```
E compare o tempo para retornar o resultado
```
db.bigdata.find({"account_no": 69271}).explain("executionStats").executionStats.executionTimeMillis
```
Para apagar o index
```
db.bigdata.dropIndex({"account_no":1})
```

## Agregação

Os operadores $sort e $count são exemplos de operações aplicaveis 
em agregações. 

```
db.marks.aggregate([{"$limit":2}])

db.marks.aggregate([{"$sort":{"marks":1}}])
db.marks.aggregate([{"$sort":{"marks":-1}}])
```

Agregaçao geralmente envolve mais de um comando de agregação, para isso podemos definir um pipeline, isto é, operaões dentro de um array
 
```
 db.marks.aggregate([
{"$sort":{"marks":-1}},
{"$limit":2}
])
```

e

db.marks.aggregate([
{
    "$group":{
        "_id":"$subject",
        "average":{"$avg":"$marks"}
        }
}
])

que é igual  a
```
SELECT subject, average(marks)
FROM marks
GROUP BY subject
```

finding the average marks per student.
sorting the output based on average marks in descending order.
limiting the output to two documents.

db.marks.aggregate([
{
    "$group":{
        "_id":"$name",
        "average":{"$avg":"$marks"}
        }
},
{
    "$sort":{"average":-1}
},
{
    "$limit":2
}
])

# Biblioteca Pymongo

Para usar o mongodb a partir do python podemos usar a biblioteca 
pymongo.  
```
python3 -m pip install pymongo 
```
Inice o db mongo (sudo systemctl start mongod)

## Conectando ao Mongodb com o Python 

No script mongo_connect.py esta um exemplo de como se conectar ao mongo.

## Realizando queries com Python 


### Inserindo documentos

No script mongo_connect.py conectamos e inserimos um arquivo com o comando insert_one, para inserir varios usamos o insert_many

```
db = client.bank

# Get a reference to 'accounts' collection
accounts_collection = db.accounts

new_accounts = [
    {
        "account_id": "MDB011235813",
        "account_holder": "Ada Lovelace",
        "account_type": "checking",
        "balance": 60218,
    },
    {
        "account_id": "MDB829000001",
        "account_holder": "Muhammad ibn Musa al-Khwarizmi",
        "account_type": "savings",
        "balance": 267914296,
    },
]

# Write an expression that inserts the documents in 'new_accounts' into the 'accounts' collection.
result = accounts_collection.insert_many(new_accounts)

document_ids = result.inserted_ids
print("# of documents inserted: " + str(len(document_ids)))
print(f"_ids of inserted documents: {document_ids}")

client.close()
```

### Lendo documentos

Para ler documentos existem os comandos find_one e find para ler um e varios documentos respectivamente.
Para ler um documento
```
db = client.bank

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts

# Query by ObjectId
document_to_find = {"_id": ObjectId("62d6e04ecab6d8e1304974ae")}

# Write an expression that retrieves the document matching the query constraint in the 'accounts' collection.
result = accounts_collection.find_one(document_to_find)
pprint.pprint(result)

client.close()
```

Para ler varios documentos

```
db = client.bank

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts

# Query
documents_to_find = {"balance": {"$gt": 4700}}

# Write an expression that selects the documents matching the query constraint in the 'accounts' collection.
cursor = accounts_collection.find(documents_to_find)

num_docs = 0
for document in cursor:
    num_docs += 1
    pprint.pprint(document)
    print()
print("# of documents found: " + str(num_docs))

client.close()
```

### Atualizando documentos

Para atualizarmos um documento e varios documentos existem os comandos update_one e update_many respectivamente. Para atualizar um documento
```
db = client.bank

# Get reference to 'accounts' collection
accounts_collection = db.accounts

# Filter
document_to_update = {"_id": ObjectId("62d6e04ecab6d8e130497482")}

# Update
add_to_balance = {"$inc": {"balance": 100}}

# Print original document
pprint.pprint(accounts_collection.find_one(document_to_update))

# Write an expression that adds to the target account balance by the specified amount.
result = accounts_collection.update_one(document_to_update, add_to_balance)
print("Documents updated: " + str(result.modified_count))

# Print updated document
pprint.pprint(accounts_collection.find_one(document_to_update))

client.close()
```
Note que usamos o operador $inc para incrementar o atributo balanço. Podemos usar diferentes operadores para atualizar como por exemplo o $set que insere (ou atualiza caso este atributo já exista), push que insere o valor em um array. No exemplo abaixo é atualizado varios documentos

```
db = client.bank

# Get reference to 'accounts' collection
accounts_collection = db.accounts

# Filter
select_accounts = {"account_type": "savings"}

# Update
set_field = {"$set": {"minimum_balance": 100}}

# Write an expression that adds a 'minimum_balance' field to each savings acccount and sets its value to 100.
result = accounts_collection.update_many(select_accounts, set_field)

print("Documents matched: " + str(result.matched_count))
print("Documents updated: " + str(result.modified_count))
pprint.pprint(accounts_collection.find_one(select_accounts))

client.close()
``` 

### Deletando Documentos
Para deletar também podemos deletar apenas um documento ou varios.
```
document_to_delete = {"_id": ObjectId("62d6e04ecab6d8e130497485")}

# Write an expression that deletes the target account.
result = accounts_collection.delete_one(document_to_delete)
```
E para varios

```
documents_to_delete = {"balance": {"$lt": 2000}}
result = accounts_collection.delete_many(documents_to_delete)
```

## Realizando Transações

A atomicidade no mongodb é apenas valida para um mesmo documento. Para implementar a atomicidade multidocumentos foi 
criado a noção de transação. A seguir um exemplo
```
client = MongoClient(MONGODB_URI)

# Step 1: Define the callback that specifies the sequence of operations to perform inside the transactions.
def callback(
    session,
    transfer_id=None,
    account_id_receiver=None,
    account_id_sender=None,
    transfer_amount=None,
):

    # Get reference to 'accounts' collection
    accounts_collection = session.client.bank.accounts

    # Get reference to 'transfers' collection
    transfers_collection = session.client.bank.transfers

    transfer = {
        "transfer_id": transfer_id,
        "to_account": account_id_receiver,
        "from_account": account_id_sender,
        "amount": {"$numberDecimal": transfer_amount},
    }

    # Transaction operations
    # Important: You must pass the session to each operation

    # Update sender account: subtract transfer amount from balance and add transfer ID
    accounts_collection.update_one(
        {"account_id": account_id_sender},
        {
            "$inc": {"balance": -transfer_amount},
            "$push": {"transfers_complete": transfer_id},
        },
        session=session,
    )

    # Update receiver account: add transfer amount to balance and add transfer ID
    accounts_collection.update_one(
        {"account_id": account_id_receiver},
        {
            "$inc": {"balance": transfer_amount},
            "$push": {"transfers_complete": transfer_id},
        },
        session=session,
    )

    # Add new transfer to 'transfers' collection
    transfers_collection.insert_one(transfer, session=session)

    print("Transaction successful")

    return


def callback_wrapper(s):
    callback(
        s,
        transfer_id="TR218721873",
        account_id_receiver="MDB343652528",
        account_id_sender="MDB574189300",
        transfer_amount=100,
    )


# Step 2: Start a client session
with client.start_session() as session:
    # Step 3: Use with_transaction to start a transaction, execute the callback, and commit (or cancel on error)
    session.with_transaction(callback_wrapper)


client.close()
```
No link https://learn.mongodb.com/courses/mongodb-crud-operations-in-python é apresentado tais comandos no pthon em detalhes.

## Criando Schemas