from pymongo import MongoClient

def dbsearch():
    client = MongoClient()
    HHdb = client['HHdb']
    vaccoll = HHdb['vaccoll']
    
    curitem = input('Enter currency: ')
    minsalary = input('Enter min. salary: ')
    item = HHdb.vaccol.find( {$and: [{'Предполагаемая зарплата (мин.)': {$lt : minsalary}},\
                             {'валюта':curitem}]})

    return item

    