from sentence_transformers import SentenceTransformer
import chromadb

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load database
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection("dream2plan")

while True:

    query = input("\nAsk a question (type exit to quit): ")

    if query.lower() == "exit":
        break

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    print("\nTop Relevant Chunks:\n")

    for i in range(len(results["documents"][0])):

        source = results["metadatas"][0][i]["source"]
        document = results["documents"][0][i]

        print(f"\nSource: {source}")
        print("-" * 50)
        print(document[:400])