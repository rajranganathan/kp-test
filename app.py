
#!/usr/bin/env python
'''
Program to find the Entity value for a parent key from Google Cloud Datastore.
In this example, parent key value is retrieved for Kind:Pet and Key Pet_id:Cherie from Datastore
'''

from google.cloud import datastore
client = datastore.Client()

#Entities with kinds- person, pet, toy
my_entities = [
{"kind": "Person", "Person_id": "Lucy", "sex": "f","age": 18},
{"kind": "Pet", "Pet_id": "Cherie", "Person_id": "Lucy",
"sex": "f", "type": "dog", "age": 7},
{"kind": "Pet", "Pet_id": "Bubsy", "Person_id": "Lucy",
"sex": "m", "type": "fish", "age": 3},
{"kind": "Toy", "Toy_id": "tennis_ball", "Pet_id": "Cherie", "Person_id": "Lucy", "price": .99},
{"kind": "Toy", "Toy_id": "castle", "Pet_id": "Bubsy",
"Person_id": "Lucy", "price": 49.99},
{"kind": "Toy", "Toy_id": "rope", "Pet_id": "Cherie", "Person_id": "Lucy", "price": 10.99},
]
#Iterate through entities and set immediate parents
for entity in my_entities:
 kind = entity['kind']
 parent_key = None
 if kind == "Pet":
  parent_key = client.key("Person", entity["Person_id"])
 elif kind == "Toy":
  parent_key = client.key("Person", entity["Person_id"],
                          "Pet", entity["Pet_id"])
 key = client.key(kind,
     entity[kind+"_id"],
     parent=parent_key) #Notice I set the parent key!!
 datastore_ent = datastore.Entity(key)
 datastore_ent.update(entity) #Include properties+id
 client.put(datastore_ent)


query1 = client.query(kind="Pet")
query1.add_filter("Pet_id", "=", "Cherie")
pet = list(query1.fetch())[0] # We know there is only one Cherie
print('Cherie’s parent: ' + str(pet.key.parent.id_or_name))

from flask import Flask
app = Flask('hello-cloudbuild')

@app.route('/')
def hello():
  return "Hello DATASTORE User !!!, \n" + 'Cherie’s parent: ' + str(pet.key.parent.id_or_name)

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)
