import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer

# Load dataset
df = pd.read_csv("processed_data.csv")

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load faiss index....
index = faiss.read_index("bank_faq.index")

def get_answer(user_query, top_k=5):
    query_embedding = model.encode([user_query],convert_to_numpy=True).astype("float32")
    distances, indices = index.search(query_embedding,top_k)

    top_matches = []
    for distance, idx in zip(distances[0],indices[0]):
        similarity = round((1 / (1 + distance)) * 100, 2)

        top_matches.append({
            "Question": df.iloc[idx]["Question"],
            "Answer": df.iloc[idx]["Answer"],
            "Category": df.iloc[idx]["Section"],
            "Similarity": similarity
        })

    best_idx = indices[0][0]
    best_distance = distances[0][0]

    best_similarity = round((1 / (1 + best_distance)) * 100, 2)

    return {
        "Answer": df.iloc[best_idx]["Answer"],
        "Category": df.iloc[best_idx]["Section"],
        "Similarity": best_similarity,
        "Top Matches": top_matches
    }
