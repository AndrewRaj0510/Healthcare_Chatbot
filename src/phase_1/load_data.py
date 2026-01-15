import pandas as pd

# Load dataset
DATA_PATH = "data/raw/medquad.csv"
df = pd.read_csv(DATA_PATH)

# Basic info
print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

print("\nSample rows:")
print(df.head(5))

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nDuplicate questions:")
print(df["question"].duplicated().sum())

# Look for strong diagnostic language
diagnostic_keywords = [
    "you have",
    "this means you have",
    "this confirms",
    "diagnosed with",
    "definitely",
    "will cause"
]

def find_diagnostic_sentences(text):
    text = str(text).lower()
    return any(keyword in text for keyword in diagnostic_keywords)

df["diagnostic_flag"] = df["answer"].apply(find_diagnostic_sentences)

print("\nPotential diagnostic answers:")
print(df[df["diagnostic_flag"] == True][["question", "answer"]].head(10))