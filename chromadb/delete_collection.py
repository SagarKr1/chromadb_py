import chromadb

client = chromadb.PersistentClient(path='./data/doc')

client.delete_collection(name='demo1')

print("Collection Deleted Successfully")