from pymongo import MongoClient

username = ''
password = ''
ip = ''
port = ''

database = ''
collection = ''

# authorization database, mostly admin or your own database
auth_db_source = ''

mongo_uri = f'mongodb://{username}:{password}@{ip}:{port}/?authMechanism=DEFAULT&authSource={auth_db_source}'


myclient = MongoClient(mongo_uri)
mydb = myclient[f'{database}']
mycol = mydb[f'{collection}']

data_to_search = ''
new_data_value = ''

field = ''
sub_field = ''

# Search a document, which has certain data in its field/sub field
filter_condition = {f'{field}.{sub_field}': f',{data_to_search}'}
document = mycol.find_one(filter_condition)

# Uncomment below carefully as it would update the field of the collection
# result = mycol.update_one(filter_condition, {'$set': {f'{field}.{sub_field}': new_data_value}})