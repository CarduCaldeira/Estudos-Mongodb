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

$sort
$count

db.marks.aggregate([{"$limit":2}])

db.marks.aggregate([{"$sort":{"marks":1}}])
db.marks.aggregate([{"$sort":{"marks":-1}}])

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

## Conectando ao Python 

python3 -m pip install pymongo

inicie o mongo
mongosh

crie um script mongo_connect.py

mongo_connect.py

----------------------------------------------------------------------------------

connect to the mongodb server.
select a database named training.
select a collection named python.
insert a sample document.
query all the documents in the training database and python collection.
close the connection to the server.

mongo_query.py

----------------------------------------------------------------------------------

Write a Python program that can:

connect to the mongodb server.
select a database named training.
select a collection named mongodb_glossary.
insert the following documents into the collection mongodb_glossary.
{“database”:”a database contains collections”}

{“collection”:”a collection stores the documents”}

{“document”:”a document contains the data in the form of key value pairs.”}

query and print all the documents in the training database and mongodb_glossary collection.

exercise.py