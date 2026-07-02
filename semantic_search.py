import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

df = pd.read_csv("processed_data.csv")

#****************Build model*********************
model = SentenceTransformer("all-MiniLM-L6-v2") # Lightweight, free and popular model...

#*************************Convert every question into vector*********************
questions = df["Question"].tolist()  # convert into a list of all questions.......
ques_embedding = model.encode(questions,convert_to_tensor=True)


