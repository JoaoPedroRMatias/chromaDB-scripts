import chromadb


client = chromadb.HttpClient(host='', port=80)
collection_name = ""

try:
    collection = client.create_collection(name=collection_name)
    print(f"Coleção '{collection_name}' criada com sucesso!")

except Exception as e:
    print("Erro ao criar a coleção:")
    print(e)
