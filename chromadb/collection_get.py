import chromadb

client = chromadb.PersistentClient(path='./data/doc')

collection = client.get_or_create_collection(name="demo1")

results = collection.query(
    query_texts=['loyal'],
    n_results=2
)

print(results)