from pathlib import Path

DATA_FOLDER = "data"

files = list(Path(DATA_FOLDER).glob("*.txt"))

for file in files:
    print(f"\n{'='*50}")
    print(f"Document: {file.name}")
    print(f"{'='*50}")

    text = file.read_text(encoding="utf-8")

    print(text[:500])