from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client['mydb1']
mydb2 = db.mydb2
# mydb2.insert_many([{'name':"test abc",
#                    'size': 900,
#                    'author': "John Pet"},
#                    {'name':"Name space",
#                    'size': 1500,
#                    'author': "Peter Pan",
#                      'age': 56}
#                    ])
# print(mydb2.count_documents({'name':'test abc'}))
mydb2.delete_many({'size': {'$gt':1500}})
objects = mydb2.find().sort('size')
for i in objects:
    print(i)
