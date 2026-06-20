from pathlib import Path

CHUNK_SIZE = 500
OVERLAP = 100

files = list(Path("data").glob("*.txt"))

all_chunks = []

for file in files:

    text = file.read_text(encoding="utf-8")

    start = 0
    chunks = []

    while start < len(text):
        end = start + CHUNK_SIZE
        chunk = text[start:end]

        chunks.append(chunk)
        all_chunks.append({
            "source": file.name,
            "content": chunk
        })

        start += CHUNK_SIZE - OVERLAP

    print(f"{file.name} -> {len(chunks)} chunks")

print(f"\nTotal Chunks Created: {len(all_chunks)}")