from sentence_transformers import SentenceTransformer
import chromadb
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Gemini model
llm = genai.GenerativeModel(
    "models/gemini-2.5-flash"
)

# Embedding model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# ChromaDB
client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_collection(
    "dream2plan"
)

print("Dream2Plan RAG Chatbot Started!")
print("Type 'exit' to quit.\n")

while True:

    question = input("Ask a question: ")

    if question.lower() == "exit":
        break

    query_embedding = embedding_model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    context = "\n\n".join(results["documents"][0])

    sources = list(
        set(
            meta["source"]
            for meta in results["metadatas"][0]
        )
    )

    prompt = f"""
You are Dream2Plan, a startup planning assistant.

Answer ONLY using the provided context.

If the answer is not available in the context,
reply exactly:

I could not find information about this in the provided documents.

Context:
{context}

Question:
{question}
"""

    response = llm.generate_content(prompt)

    print("\nAnswer:")
    print(response.text)

    if "I could not find information" in response.text:
        print("\nSources: None")
    else:
        print("\nSources:")
        for source in sources:
            print("-", source)

    print("\n" + "=" * 60 + "\n")