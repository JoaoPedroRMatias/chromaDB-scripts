import chromadb


client = chromadb.HttpClient(host='', port=80)
collections = client.list_collections()

for collection in collections:
    print(collection)