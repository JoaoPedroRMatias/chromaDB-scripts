import chromadb


try:
    client = chromadb.HttpClient(host='', port=80)
    collection_name = ""
    collections = client.list_collections()
    
    client.delete_collection(collection_name)
    print(f"Coleção '{collection_name}' apagada com sucesso!")

except Exception as e:
    print("Falha ao conectar ao Chroma DB ou ao apagar a coleção.")
    print("Erro:", e)