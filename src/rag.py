from sentence_transformers import SentenceTransformer
import chromadb
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import os

# Load local .env
load_dotenv()

# Get API key
api_key = os.getenv("GOOGLE_API_KEY")

# If running on Streamlit Cloud
if api_key is None:
    api_key = st.secrets["GOOGLE_API_KEY"]

# Configure Gemini
genai.configure(api_key=api_key)

# Gemini Model
llm = genai.GenerativeModel("models/gemini-2.5-flash")

# Embedding Model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# ChromaDB Connection
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection("dream2plan")

def get_answer(question):
    try:
        # Create query embedding
        query_embedding = embedding_model.encode(question).tolist()

        # Retrieve relevant chunks
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=5
        )

        retrieved_chunks = results["documents"][0]

        context = "\n\n".join(retrieved_chunks)

        sources = sorted(
            set(meta["source"] for meta in results["metadatas"][0])
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

        return response.text, sources

    except Exception as e:
        return f"Error: {str(e)}", []