import pandas as pd
import re

DATA_PATH = "data/raw/medquad.csv"
OUTPUT_PATH = "data/processed/medquad_cleaned.csv"

df = pd.read_csv(DATA_PATH)

REPLACEMENTS = {
    r"\byou have\b": "this may be related to",
    r"\bthis means you have\b": "this could indicate",
    r"\bthis confirms\b": "this could suggest",
    r"\bdiagnosed with\b": "evaluated for",
    r"\bdefinitely\b": "possibly",
    r"\bwill cause\b": "may cause"
}

def normalize_answer(text):
    text = str(text)
    text_lower = text.lower()

    for pattern, replacement in REPLACEMENTS.items():
        text_lower = re.sub(pattern, replacement, text_lower)

    disclaimer = (
        "\n\nThis information is for educational purposes only and "
        "is not a confirmed medical diagnosis. Please consult a qualified "
        "healthcare professional for proper evaluation and treatment."
    )

    return text_lower.strip() + disclaimer

df["answer"] = df["answer"].apply(normalize_answer)

df.to_csv(OUTPUT_PATH, index=False)
print("✅ Cleaned dataset saved:", OUTPUT_PATH)