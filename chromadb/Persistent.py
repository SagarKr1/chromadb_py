import chromadb

client = chromadb.PersistentClient(path="./data/doc")

collection = client.create_collection(name="demo1")

collection.add(
    ids=["cat","dog","cow"],
    documents=[
        "Cat are lovely but not loyal",
        'Dogs are loyal and protective',
        'Cows are sweet and give milk'
    ],
    metadatas=[
        {"description":"This is only for demo"},
        {"description":"This is only for demo"},
        {"description":"This is only for demo"}
    ]
)

results = collection.query(
    query_texts=['I like milk'],
    n_results=2
)

print(results)