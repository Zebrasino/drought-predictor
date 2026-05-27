import pandas as pd

df = pd.read_csv("data/raw/drought.csv")
df = df.dropna()
df = df.drop(columns=["fips", "date"], errors="ignore")
df["score"] = df["score"].round().astype(int)

print("Classi dopo dropna:")
print(df["score"].value_counts().sort_index())
print("---")
print(f"Classi uniche: {sorted(df['score'].unique())}")