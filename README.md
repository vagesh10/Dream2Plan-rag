# Dream2Plan RAG Chatbot

## Project Overview

Dream2Plan is an AI-powered Startup Knowledge Assistant built using Retrieval-Augmented Generation (RAG). The chatbot allows users to ask questions related to startup planning, funding, legal requirements, government schemes, market research, and business model development.

The system retrieves relevant information from a custom knowledge base and generates grounded answers using Google's Gemini Large Language Model. Answers are supported by source citations from the original documents.

---

## Features

* Document-based Question Answering
* Retrieval-Augmented Generation (RAG)
* Semantic Search using Vector Embeddings
* ChromaDB Vector Database
* Google Gemini Integration
* Source Citations
* Interactive Command Line Interface
* Handles Out-of-Scope Questions

---

## Knowledge Base Documents

The chatbot uses the following documents:

1. market_research.txt
2. funding_options.txt
3. legal_requirements.txt
4. government_schemes.txt
5. business_model_canvas.txt

---

## Tech Stack

### Programming Language

* Python 3.11

### Libraries

* sentence-transformers
* chromadb
* google-generativeai
* python-dotenv
* pypdf
* langchain

### Models

Embedding Model:

* all-MiniLM-L6-v2

LLM:

* Gemini 2.5 Flash

Vector Database:

* ChromaDB

---

## Architecture

Document Ingestion
↓
Text Chunking
↓
Embedding Generation
↓
ChromaDB Vector Storage
↓
User Question
↓
Similarity Search
↓
Relevant Context Retrieval
↓
Gemini Answer Generation
↓
Answer + Citations

---

## Chunking Strategy

A fixed-size chunking strategy was used.

* Chunk Size: 500 characters
* Overlap: 100 characters

The overlap helps preserve context between adjacent chunks and improves retrieval quality.

---

## Embedding Model

The project uses:

all-MiniLM-L6-v2

Reasons:

* Lightweight
* Fast inference
* High semantic search accuracy
* Suitable for beginner RAG systems

---

## Vector Database

ChromaDB was selected because:

* Easy integration with Python
* Persistent storage support
* Fast similarity search
* Beginner-friendly implementation

The vector database is stored locally and reused across sessions.

---

## Project Structure

Dream2Plan-rag/

├── data/

│   ├── market_research.txt

│   ├── funding_options.txt

│   ├── legal_requirements.txt

│   ├── government_schemes.txt

│   └── business_model_canvas.txt

├── chroma_db/

├── src/

│   ├── ingest.py

│   ├── chunking.py

│   ├── index_documents.py

│   ├── query.py

│   └── rag.py

├── requirements.txt

├── .env

└── README.md

---

## Installation

### Clone Repository

```bash
git clone <your-repository-url>
cd Dream2Plan-rag
```

### Create Virtual Environment

```bash
py -3.11 -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a .env file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Important:

Never commit your API key to GitHub.

---

## Build Vector Database

Run:

```bash
python src/index_documents.py
```

This will:

* Load documents
* Create chunks
* Generate embeddings
* Store vectors in ChromaDB

---

## Run Chatbot

```bash
python src/rag.py
```

---

## Example Queries

### Startup Funding

How can I get funding for my startup?

### Legal Requirements

What is DPIIT recognition?

### Government Support

What government schemes support startups?

### Business Planning

What are revenue streams?

### Market Research

Which startup sectors are growing in India?

---

## Out-of-Scope Example

Question:

Who won the FIFA World Cup 2022?

Response:

I could not find information about this in the provided documents.

---

## Known Limitations

* Uses fixed-size chunking instead of semantic chunking.
* Limited to the uploaded document collection.
* Cannot answer questions outside the knowledge base.
* Retrieval quality depends on document quality and chunk size.

---

## Future Improvements

* Streamlit Web Interface
* Hybrid Search (Keyword + Vector Search)
* PDF and DOCX Support
* Conversation Memory
* Multi-document Citations
* Re-ranking for Better Retrieval

---

## Author

Vagesh Kumar Surla

AI Engineering Intern Assignment

Dream2Plan RAG Chatbot
