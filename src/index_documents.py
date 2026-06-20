from pathlib import Path
from sentence_transformers import SentenceTransformer
import chromadb

CHUNK_SIZE = 500
OVERLAP = 100

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="dream2plan"
)

documents = []
metadatas = []
ids = []

chunk_id = 0

files = list(Path("data").glob("*.txt"))

for file in files:

    text = file.read_text(encoding="utf-8")

    start = 0

    while start < len(text):

        end = start + CHUNK_SIZE

        chunk = text[start:end]

        documents.append(chunk)

        metadatas.append({
            "source": file.name
        })

        ids.append(f"chunk_{chunk_id}")

        chunk_id += 1

        start += CHUNK_SIZE - OVERLAP


print(f"Creating embeddings for {len(documents)} chunks...")

embeddings = model.encode(
    documents,
    batch_size=32,
    show_progress_bar=True
).tolist()

collection.add(
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas,
    ids=ids
)

print("Indexing Complete!")
print(f"Stored {len(documents)} chunks.")