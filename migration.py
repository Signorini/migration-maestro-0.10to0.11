
URL = 'mongodb://localhost:27017/'
DBNAME = 'maestro'




from pymongo import MongoClient
from pymongo import InsertOne, UpdateOne
from bson.objectid import ObjectId

client = MongoClient(URL)
db = client[DBNAME]

apps = db.applications
servers = db.servers


for app in apps.find({ 'servers': { '$exists': True} }):
    if 'servers' in app and app['servers']:
        if len(app['servers']) > 0:
            napp = app.copy()
            del napp['servers']
            del napp['updated_at']

            napp['servers'] = []
            for svs in app['servers']:
                napp['servers'].append(ObjectId(svs))
            
            result = db.applications.update_one({'_id': app['_id']}, {'$set':napp, '$currentDate': { 'updated_at': True }}, upsert=True)
            print(result.raw_result)


supdated = []
for server in servers.find({}):
    nserver = server.copy()
    if 'cpu' in server and server['cpu']:
        nserver['cpu'] = int(server['cpu'])
    if 'memory' in server and server['memory']:
        nserver['memory'] = int(server['memory'])

    del nserver['updated_at']
    result = db.servers.update_one({'_id': server['_id']}, {'$set': nserver, '$currentDate': { 'updated_at': True }}, upsert=False)
    print(result.raw_result)