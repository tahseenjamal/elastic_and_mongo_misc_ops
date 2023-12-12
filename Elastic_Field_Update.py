import requests

host  = ''
port = ''
user = ''
password = ''

elasticsearch_url = f'http://{user}:{password}@{host}:{port}'

# User index name with * like access.log* so that all logs are considered
index_name = ''
headers = {'Content-Type': 'application/json'}

original_data = ''
replacement_data = ''

search_url = f'{elasticsearch_url}/{index_name}/_search'
query = { 'query': { 'match': { 'message.keyword': f',{original_data}' } } }

response = requests.post(search_url, headers=headers, json=query)

if response.status_code == 200:
    search_results = response.json()
    if len(search_results['hits']['hits']) > 0:
        hit = search_results['hits']['hits'][0]
        hit_index = hit['_index']
        id = hit['_id']

        # In place of _update you can use _doc, if you want to update full document
        update_url = f'{elasticsearch_url}/{hit_index}/_update/{id}'
        new_message_value = f',{replacement_data}'
        update_query = { 'doc': { 'message': new_message_value } }
        
        # Uncomment below this only when you want to update
        # response = requests.post(update_url, json=update_query)   
        

