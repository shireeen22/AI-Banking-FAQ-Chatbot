import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# load the df

df = pd.read_csv("processed_data.csv")

# build a model.....
model = SentenceTransformer("all-MiniLM-L6-v2")

# embedding.....
questions = df["Question"].tolist()

embeddings = model.encode(questions,convert_to_numpy=True) # using convert_to_numpy here....
# Convert into float32 which is required for FAISS........
embeddings = embeddings.astype("float32") 

# dimension.....

dimension = embeddings.shape[1]
# index...
index = faiss.IndexFlatL2(dimension)

# add embeddings....
index.add(embeddings)

# save....
faiss.write_index(index,"bank_faq.index")

print("FAISS index created successfully!")
print("Total vectors:", index.ntotal)  # Total vectors: 999