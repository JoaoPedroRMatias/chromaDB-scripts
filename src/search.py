import chromadb

try:
    client = chromadb.HttpClient(host='', port=80)

    collection_name = ""
    collection = client.get_collection(name=collection_name)
    dados = collection.get()

    documentos = dados["documents"]
    print(f"Possui: {len(documentos)} documentos na collection {collection_name}")

except Exception as e:
    print("Erro ao tentar acessar a coleção ou contar os documentos:")
    print(e)
