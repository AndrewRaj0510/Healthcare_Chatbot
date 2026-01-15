import pandas as pd
from pathlib import Path

INPUT_PATH = "data/processed/medquad_cleaned.csv"
OUTPUT_PATH = "data/processed/healthcare_documents.txt"

df = pd.read_csv(INPUT_PATH)

def build_document(row):
    doc = f"""
Topic: {row['focus_area']}

Question:
{row['question']}

Educational Information:
{row['answer']}

Source:
{row['source']}
""".strip()

    return doc

documents = df.apply(build_document, axis=1)

# Ensure output directory exists
Path("data/processed").mkdir(parents=True, exist_ok=True)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    for doc in documents:
        f.write(doc)
        f.write("\n\n" + "="*80 + "\n\n")

print(f"✅ Knowledge documents saved to {OUTPUT_PATH}")
print(f"📄 Total documents created: {len(documents)}")