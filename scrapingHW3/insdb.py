from pymongo import MongoClient

def insert_to_db(vacs):
	client = MongoClient()
	HHdb = client['HHdb']
	vaccoll = HHdb['vaccoll']

	HHdb.vaccoll.insert_many(vacs)
	print(f'{len(vacs)} was inserted to database')

