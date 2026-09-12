from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings


# -----------------------------------
# 1. LOAD PDF
# -----------------------------------

path = "E:/document/pdf/hr_policy.pdf"

pdf_loader = PyPDFLoader(path)

print("✅ PDF loader initialized.")

pdf_data = pdf_loader.load()

print(f"✅ PDF loaded successfully. Total pages: {len(pdf_data)}")


# -----------------------------------
# 2. SPLIT DOCUMENT INTO CHUNKS
# -----------------------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=50
)

print("✅ Text splitter initialized.")

chunks = splitter.split_documents(pdf_data)

print(f"✅ Chunks created successfully. Total chunks: {len(chunks)}")


# -----------------------------------
# 3. LOAD EMBEDDING MODEL
# -----------------------------------

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={
        "device": "cpu"
    },
    encode_kwargs={
        "normalize_embeddings": True
    }
)

print("✅ Embedding model loaded successfully.")


# -----------------------------------
# 4. CREATE EMBEDDINGS
# -----------------------------------

chunk_texts = [
    chunk.page_content
    for chunk in chunks
]

vectors = embedding.embed_documents(chunk_texts)

print("✅ Embeddings created successfully.")


# -----------------------------------
# 5. CHECK RESULT
# -----------------------------------

if vectors:
    print(
        f"Vectors: {len(vectors)} chunks × "
        f"{len(vectors[0])} dimensions"
    )

    print(
        "First vector, first 10 values:",
        vectors[0][:10]
    )