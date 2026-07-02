import pandas as pd
import numpy as np
from datetime import datetime
import os

def save_feedback(question, answer, feedback):
    data = {
        "question":question,
        "answer":answer,
        "feedback":feedback,
        "timestamp":datetime.now()
    }

    # create a df....
    new_row = pd.DataFrame([data])


    if os.path.exists("feedback.csv"):
        new_row.to_csv(
            "feedback.csv",
            mode="a",
            header=False,
            index=False
        )
    else:
        new_row.to_csv(
            "feedback.csv",
            index=False
        )