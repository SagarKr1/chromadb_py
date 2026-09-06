import chromadb

# CREATE A CHROMA  CLIENT
client = chromadb.Client()

# CREATE A COLLECTION WHERE WE CAN STORE OUR DATA
collection = client.create_collection(name="my_collection")

# CREATE A COLLECTION
collection.add(
    ids=['dog','cat'],
    documents=[
        'Dogs are loyal and protective.',
        'cats are lovely but not loyal'
    ],
    metadatas=[
        {"description": "This is only for demo"},
        {"description": "Same here"}
    ]
)

# QUERY
result = collection.query(
    query_texts=['rat'],
    n_results=2
)

print(result)