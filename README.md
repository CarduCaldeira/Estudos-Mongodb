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