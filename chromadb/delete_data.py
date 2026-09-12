import chromadb

client = chromadb.PersistentClient(path='./data/doc')

collection = client.get_or_create_collection(name="Test")

# create data
collection.add(
    ids=['cat','dog'],
    documents=[
        "cat say meow",
        "dog say Barks"
    ]
)

# delete data
collection.delete(
    ids=['cat','dog']
)

# delete collection
client.delete_collection(
    name="Test"
)